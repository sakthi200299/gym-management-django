from trainers.repository import trainer_repository
from trainers.dto.trainer_request_dto import TrainerRequestDTO
from trainers.mapper.trainer_mapper import TrainerMapper


def create_trainer(dto: TrainerRequestDTO) -> dict:
    if not dto.name:
        raise ValueError("Name is required")
    if not dto.email:
        raise ValueError("Email is required")
    if not dto.phone:
        raise ValueError("Phone is required")
    if not dto.specialization:
        raise ValueError("Specialization is required")
    if not dto.experience_years:
        raise ValueError("Experience years is required")
    if trainer_repository.exists_by_email(dto.email):
        raise ValueError(f"Trainer with email '{dto.email}' already exists")
    trainer = trainer_repository.save(TrainerMapper.to_entity(dto))
    return TrainerMapper.to_response_dto(trainer).to_dict()


def update_trainer(trainer_id: int, dto: TrainerRequestDTO) -> dict:
    trainer = trainer_repository.find_by_id(trainer_id)
    if not trainer:
        raise ValueError(f"Trainer with id {trainer_id} not found")
    trainer = trainer_repository.update(trainer, TrainerMapper.to_entity(dto))
    return TrainerMapper.to_response_dto(trainer).to_dict()


def get_all_trainers() -> list:
    trainers = trainer_repository.find_all_objects()
    if not trainers:
        raise ValueError("No trainers found")
    return TrainerMapper.to_response_dto_list(trainers)


def get_trainer_by_id(trainer_id: int) -> dict:
    trainer = trainer_repository.find_by_id(trainer_id)
    if not trainer:
        raise ValueError(f"Trainer with id {trainer_id} not found")
    return TrainerMapper.to_response_dto(trainer).to_dict()
