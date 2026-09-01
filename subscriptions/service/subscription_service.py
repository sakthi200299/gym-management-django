from subscriptions.repository import subscription_repository
from subscriptions.dto.subscription_request_dto import SubscriptionRequestDTO
from subscriptions.mapper.subscription_mapper import SubscriptionMapper
from users.repository.user_repository import find_by_id as find_user
from plans.repository.plan_repository import find_by_id as find_plan


def create_subscription(dto: SubscriptionRequestDTO) -> dict:
    if not dto.user_id:
        raise ValueError("User id is required")
    if not dto.plan_id:
        raise ValueError("Plan id is required")
    if not dto.start_date:
        raise ValueError("Start date is required")
    if not dto.end_date:
        raise ValueError("End date is required")
    user = find_user(dto.user_id)
    if not user:
        raise ValueError(f"User with id {dto.user_id} not found")
    plan = find_plan(dto.plan_id)
    if not plan:
        raise ValueError(f"Plan with id {dto.plan_id} not found")
    if subscription_repository.exists_by_user(dto.user_id):
        raise ValueError(f"User with id {dto.user_id} already has an active subscription")
    sub = subscription_repository.save(user, plan, SubscriptionMapper.to_entity(dto))
    return SubscriptionMapper.to_response_dto(sub).to_dict()


def update_subscription(sub_id: int, dto: SubscriptionRequestDTO) -> dict:
    sub = subscription_repository.find_by_id(sub_id)
    if not sub:
        raise ValueError(f"Subscription with id {sub_id} not found")
    sub = subscription_repository.update(sub, SubscriptionMapper.to_entity(dto))
    return SubscriptionMapper.to_response_dto(sub).to_dict()


def get_all_subscriptions() -> list:
    subs = subscription_repository.find_all_objects()
    if not subs:
        raise ValueError("No subscriptions found")
    return SubscriptionMapper.to_response_dto_list(subs)


def get_subscription_by_id(sub_id: int) -> dict:
    sub = subscription_repository.find_by_id(sub_id)
    if not sub:
        raise ValueError(f"Subscription with id {sub_id} not found")
    return SubscriptionMapper.to_response_dto(sub).to_dict()
