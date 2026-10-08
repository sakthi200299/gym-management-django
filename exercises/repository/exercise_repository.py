from exercises.model.exercise import Exercise
from trainers.model.trainer import Trainer
from subscriptions.model.subscription import Subscription


def save(trainer: Trainer, subscription: Subscription, data: dict) -> Exercise:
    return Exercise.objects.create(trainer=trainer, subscription=subscription, **data)


def update(exercise: Exercise, data: dict) -> Exercise:
    for key, value in data.items():
        setattr(exercise, key, value)
    exercise.save()
    return exercise


def find_all_objects() -> list:
    return list(Exercise.objects.select_related('trainer', 'subscription__user', 'subscription__plan').all())


def find_by_id(exercise_id: int) -> Exercise | None:
    return Exercise.objects.select_related('trainer', 'subscription__user', 'subscription__plan').filter(id=exercise_id).first()


def exists_by_name_and_subscription(name: str, subscription_id: int) -> bool:
    return Exercise.objects.filter(name=name, subscription_id=subscription_id).exists()


def delete(exercise: Exercise) -> None:
    exercise.delete()
