from plans.repository import plan_repository
from plans.dto.plan_request_dto import PlanRequestDTO
from plans.mapper.plan_mapper import PlanMapper


def create_plan(dto: PlanRequestDTO) -> dict:
    if not dto.name:
        raise ValueError("Name is required")
    if not dto.price:
        raise ValueError("Price is required")
    if not dto.duration:
        raise ValueError("Duration is required")
    if not dto.description:
        raise ValueError("Description is required")
    if plan_repository.exists_by_name(dto.name):
        raise ValueError(f"Plan '{dto.name}' already exists")
    plan = plan_repository.save(PlanMapper.to_entity(dto))
    return PlanMapper.to_response_dto(plan).to_dict()


def update_plan(plan_id: int, dto: PlanRequestDTO) -> dict:
    plan = plan_repository.find_by_id(plan_id)
    if not plan:
        raise ValueError(f"Plan with id {plan_id} not found")
    plan = plan_repository.update(plan, PlanMapper.to_entity(dto))
    return PlanMapper.to_response_dto(plan).to_dict()


def get_all_plans() -> list:
    plans = plan_repository.find_all_objects()
    if not plans:
        raise ValueError("No plans found")
    return PlanMapper.to_response_dto_list(plans)


def get_plan_by_id(plan_id: int) -> dict:
    plan = plan_repository.find_by_id(plan_id)
    if not plan:
        raise ValueError(f"Plan with id {plan_id} not found")
    return PlanMapper.to_response_dto(plan).to_dict()
