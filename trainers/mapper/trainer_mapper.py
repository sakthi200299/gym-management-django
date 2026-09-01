from trainers.dto.trainer_request_dto import TrainerRequestDTO
from trainers.dto.trainer_response_dto import TrainerResponseDTO
from trainers.model.trainer import Trainer


class TrainerMapper:
    """
    Equivalent to TrainerMapper.java (MapStruct) in Spring Boot.
    """

    @staticmethod
    def to_entity(dto: TrainerRequestDTO) -> dict:
        return dto.to_dict()

    @staticmethod
    def to_response_dto(trainer: Trainer) -> TrainerResponseDTO:
        return TrainerResponseDTO(
            id=trainer.id,
            name=trainer.name,
            email=trainer.email,
            phone=trainer.phone,
            specialization=trainer.specialization,
            experience_years=trainer.experience_years,
        )

    @staticmethod
    def to_response_dto_list(trainers: list) -> list:
        return [TrainerMapper.to_response_dto(t).to_dict() for t in trainers]
