from plans.dto.plan_request_dto import PlanRequestDTO
from plans.dto.plan_response_dto import PlanResponseDTO
from plans.model.plan import Plan


class PlanMapper:
    """
    Equivalent to PlanMapper.java (MapStruct) in Spring Boot.
    """

    @staticmethod
    def to_entity(dto: PlanRequestDTO) -> dict:
        return dto.to_dict()

    @staticmethod
    def to_response_dto(plan: Plan) -> PlanResponseDTO:
        return PlanResponseDTO(
            id=plan.id,
            name=plan.name,
            price=plan.price,
            duration=plan.duration,
            description=plan.description,
        )

    @staticmethod
    def to_response_dto_list(plans: list) -> list:
        return [PlanMapper.to_response_dto(p).to_dict() for p in plans]
