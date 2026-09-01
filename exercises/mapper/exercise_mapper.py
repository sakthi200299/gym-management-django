from exercises.dto.exercise_request_dto import ExerciseRequestDTO
from exercises.dto.exercise_response_dto import ExerciseResponseDTO
from exercises.model.exercise import Exercise


class ExerciseMapper:
    """
    Equivalent to ExerciseMapper.java (MapStruct) in Spring Boot.
    """

    @staticmethod
    def to_entity(dto: ExerciseRequestDTO) -> dict:
        return {
            "name": dto.name,
            "category": dto.category,
            "sets": dto.sets,
            "reps": dto.reps,
            "duration_minutes": dto.duration_minutes,
        }

    @staticmethod
    def to_response_dto(exercise: Exercise) -> ExerciseResponseDTO:
        return ExerciseResponseDTO(
            id=exercise.id,
            name=exercise.name,
            category=exercise.category,
            sets=exercise.sets,
            reps=exercise.reps,
            duration_minutes=exercise.duration_minutes,
            trainer={
                "id": exercise.trainer.id,
                "name": exercise.trainer.name,
                "specialization": exercise.trainer.specialization,
            },
            subscription={
                "id": exercise.subscription.id,
                "status": exercise.subscription.status,
                "user": {"id": exercise.subscription.user.id, "name": exercise.subscription.user.name},
                "plan": {"id": exercise.subscription.plan.id, "name": exercise.subscription.plan.name},
            },
        )

    @staticmethod
    def to_response_dto_list(exercises: list) -> list:
        return [ExerciseMapper.to_response_dto(e).to_dict() for e in exercises]
