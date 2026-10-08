from subscriptions.model.subscription import Subscription
from users.model.user import User
from plans.model.plan import Plan


def save(user: User, plan: Plan, data: dict) -> Subscription:
    return Subscription.objects.create(user=user, plan=plan, **data)


def update(sub: Subscription, data: dict) -> Subscription:
    for key, value in data.items():
        setattr(sub, key, value)
    sub.save()
    return sub


def find_all_objects() -> list:
    return list(Subscription.objects.select_related('user', 'plan').all())


def find_by_id(sub_id: int) -> Subscription | None:
    return Subscription.objects.select_related('user', 'plan').filter(id=sub_id).first()


def exists_by_user(user_id: int) -> bool:
    return Subscription.objects.filter(user_id=user_id, status='active').exists()


def delete(sub: Subscription) -> None:
    sub.delete()
