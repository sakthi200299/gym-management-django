from exercises.repository import exercise_repository
from exercises.dto.exercise_request_dto import ExerciseRequestDTO
from exercises.mapper.exercise_mapper import ExerciseMapper
from trainers.repository.trainer_repository import find_by_id as find_trainer
from subscriptions.repository.subscription_repository import find_by_id as find_subscription


def create_exercise(dto: ExerciseRequestDTO) -> dict:
    if not dto.name:
        raise ValueError("Name is required")
    if not dto.category:
        raise ValueError("Category is required")
    if not dto.sets:
        raise ValueError("Sets is required")
    if not dto.reps:
        raise ValueError("Reps is required")
    if not dto.duration_minutes:
        raise ValueError("Duration minutes is required")
    if not dto.trainer_id:
        raise ValueError("Trainer id is required")
    if not dto.subscription_id:
        raise ValueError("Subscription id is required")
    trainer = find_trainer(dto.trainer_id)
    if not trainer:
        raise ValueError(f"Trainer with id {dto.trainer_id} not found")
    subscription = find_subscription(dto.subscription_id)
    if not subscription:
        raise ValueError(f"Subscription with id {dto.subscription_id} not found")
    if exercise_repository.exists_by_name_and_subscription(dto.name, dto.subscription_id):
        raise ValueError(f"Exercise '{dto.name}' already exists for this subscription")
    exercise = exercise_repository.save(trainer, subscription, ExerciseMapper.to_entity(dto))
    return ExerciseMapper.to_response_dto(exercise).to_dict()


def update_exercise(exercise_id: int, dto: ExerciseRequestDTO) -> dict:
    exercise = exercise_repository.find_by_id(exercise_id)
    if not exercise:
        raise ValueError(f"Exercise with id {exercise_id} not found")
    exercise = exercise_repository.update(exercise, ExerciseMapper.to_entity(dto))
    return ExerciseMapper.to_response_dto(exercise).to_dict()


def get_all_exercises() -> list:
    exercises = exercise_repository.find_all_objects()
    if not exercises:
        raise ValueError("No exercises found")
    return ExerciseMapper.to_response_dto_list(exercises)


def get_exercise_by_id(exercise_id: int) -> dict:
    exercise = exercise_repository.find_by_id(exercise_id)
    if not exercise:
        raise ValueError(f"Exercise with id {exercise_id} not found")
    return ExerciseMapper.to_response_dto(exercise).to_dict()
