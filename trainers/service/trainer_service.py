from django.db import transaction

from trainers.repository import trainer_repository
from trainers.serializer.trainer_serializer import TrainerSerializer


@transaction.atomic
def create_trainer(data: dict) -> dict:
    if trainer_repository.exists_by_email(data.get("email")):
        raise ValueError(f"Trainer with email '{data.get('email')}' already exists")
    trainer = trainer_repository.save(data)
    return TrainerSerializer(trainer).data


@transaction.atomic
def update_trainer(trainer_id: int, data: dict) -> dict:
    trainer = trainer_repository.find_by_id(trainer_id)
    if not trainer:
        raise ValueError(f"Trainer with id {trainer_id} not found")
    trainer = trainer_repository.update(trainer, data)
    return TrainerSerializer(trainer).data


def get_all_trainers() -> list:
    trainers = trainer_repository.find_all_objects()
    if not trainers:
        raise ValueError("No trainers found")
    return TrainerSerializer(trainers, many=True).data


def get_trainer_by_id(trainer_id: int) -> dict:
    trainer = trainer_repository.find_by_id(trainer_id)
    if not trainer:
        raise ValueError(f"Trainer with id {trainer_id} not found")
    return TrainerSerializer(trainer).data
