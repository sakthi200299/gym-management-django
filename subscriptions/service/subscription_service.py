from django.db import transaction

from subscriptions.repository import subscription_repository
from subscriptions.serializer.subscription_serializer import SubscriptionSerializer
from users.repository.user_repository import find_by_id as find_user
from plans.repository.plan_repository import find_by_id as find_plan
from config.cache_service import get_cached_subscription, set_cached_subscription, evict_subscription_cache


@transaction.atomic
def create_subscription(data: dict) -> dict:
    user = find_user(data.get("user").id if hasattr(data.get("user"), 'id') else data.get("user"))
    if not user:
        raise ValueError(f"User with id {data.get('user')} not found")
    plan = find_plan(data.get("plan").id if hasattr(data.get("plan"), 'id') else data.get("plan"))
    if not plan:
        raise ValueError(f"Plan with id {data.get('plan')} not found")
    if subscription_repository.exists_by_user(user.id):
        raise ValueError(f"User already has an active subscription")
    sub = subscription_repository.save(user, plan, {
        "start_date": data["start_date"],
        "end_date": data["end_date"],
        "status": data.get("status", "active"),
    })
    return SubscriptionSerializer(sub).data


@transaction.atomic
def update_subscription(sub_id: int, data: dict) -> dict:
    sub = subscription_repository.find_by_id(sub_id)
    if not sub:
        raise ValueError(f"Subscription with id {sub_id} not found")
    sub = subscription_repository.update(sub, {
        k: v for k, v in data.items() if k not in ['user', 'plan']
    })
    evict_subscription_cache(sub_id)                    # cache evict on update
    return SubscriptionSerializer(sub).data


def get_all_subscriptions() -> list:
    subs = subscription_repository.find_all_objects()
    if not subs:
        raise ValueError("No subscriptions found")
    return SubscriptionSerializer(subs, many=True).data


def get_subscription_by_id(sub_id: int) -> dict:
    cached = get_cached_subscription(sub_id)            # L2 Redis check
    if cached:
        return cached                                   # return from Redis — NO DB hit
    sub = subscription_repository.find_by_id(sub_id)
    if not sub:
        raise ValueError(f"Subscription with id {sub_id} not found")
    data = SubscriptionSerializer(sub).data
    set_cached_subscription(sub_id, data)               # store in Redis
    return data


@transaction.atomic
def delete_subscription(sub_id: int) -> None:
    sub = subscription_repository.find_by_id(sub_id)
    if not sub:
        raise ValueError(f"Subscription with id {sub_id} not found")
    subscription_repository.delete(sub)
    evict_subscription_cache(sub_id)                    # cache evict on delete
