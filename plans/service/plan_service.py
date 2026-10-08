from django.db import transaction

from plans.repository import plan_repository
from plans.serializer.plan_serializer import PlanSerializer
from config.cache_service import get_cached_plans, set_cached_plans, evict_plans_cache


@transaction.atomic
def create_plan(data: dict) -> dict:
    if plan_repository.exists_by_name(data.get("name")):
        raise ValueError(f"Plan '{data.get('name')}' already exists")
    plan = plan_repository.save(data)
    evict_plans_cache()                             # cache evict on create
    return PlanSerializer(plan).data


@transaction.atomic
def update_plan(plan_id: int, data: dict) -> dict:
    plan = plan_repository.find_by_id(plan_id)
    if not plan:
        raise ValueError(f"Plan with id {plan_id} not found")
    plan = plan_repository.update(plan, data)
    evict_plans_cache()                             # cache evict on update
    return PlanSerializer(plan).data


def get_all_plans() -> list:
    cached = get_cached_plans()                     # L2 Redis check
    if cached:
        return cached                               # return from Redis — NO DB hit
    plans = plan_repository.find_all_objects()
    if not plans:
        raise ValueError("No plans found")
    data = PlanSerializer(plans, many=True).data
    set_cached_plans(data)                          # store in Redis
    return data


def get_plan_by_id(plan_id: int) -> dict:
    plan = plan_repository.find_by_id(plan_id)
    if not plan:
        raise ValueError(f"Plan with id {plan_id} not found")
    return PlanSerializer(plan).data
