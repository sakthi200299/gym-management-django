from django.db import transaction

from exercises.repository import exercise_repository
from exercises.serializer.exercise_serializer import ExerciseSerializer
from trainers.repository.trainer_repository import find_by_id as find_trainer
from subscriptions.repository.subscription_repository import find_by_id as find_subscription


@transaction.atomic
def create_exercise(data: dict) -> dict:
    trainer = find_trainer(data.get("trainer"))
    if not trainer:
        raise ValueError(f"Trainer with id {data.get('trainer')} not found")
    subscription = find_subscription(data.get("subscription"))
    if not subscription:
        raise ValueError(f"Subscription with id {data.get('subscription')} not found")
    if exercise_repository.exists_by_name_and_subscription(data.get("name"), data.get("subscription")):
        raise ValueError(f"Exercise '{data.get('name')}' already exists for this subscription")
    exercise = exercise_repository.save(trainer, subscription, {
        k: v for k, v in data.items() if k not in ['trainer', 'subscription']
    })
    return ExerciseSerializer(exercise).data


@transaction.atomic
def update_exercise(exercise_id: int, data: dict) -> dict:
    exercise = exercise_repository.find_by_id(exercise_id)
    if not exercise:
        raise ValueError(f"Exercise with id {exercise_id} not found")
    exercise = exercise_repository.update(exercise, {
        k: v for k, v in data.items() if k not in ['trainer', 'subscription']
    })
    return ExerciseSerializer(exercise).data


def get_all_exercises() -> list:
    exercises = exercise_repository.find_all_objects()
    if not exercises:
        raise ValueError("No exercises found")
    return ExerciseSerializer(exercises, many=True).data


def get_exercise_by_id(exercise_id: int) -> dict:
    exercise = exercise_repository.find_by_id(exercise_id)
    if not exercise:
        raise ValueError(f"Exercise with id {exercise_id} not found")
    return ExerciseSerializer(exercise).data


@transaction.atomic
def delete_exercise(exercise_id: int) -> None:
    exercise = exercise_repository.find_by_id(exercise_id)
    if not exercise:
        raise ValueError(f"Exercise with id {exercise_id} not found")
    exercise_repository.delete(exercise)
