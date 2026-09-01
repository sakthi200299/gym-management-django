from plans.model.plan import Plan


def save(data: dict) -> Plan:
    return Plan.objects.create(**data)


def update(plan: Plan, data: dict) -> Plan:
    for key, value in data.items():
        setattr(plan, key, value)
    plan.save()
    return plan


def find_all_objects() -> list:
    return list(Plan.objects.all())


def find_by_id(plan_id: int) -> Plan | None:
    return Plan.objects.filter(id=plan_id).first()


def exists_by_name(name: str) -> bool:
    return Plan.objects.filter(name=name).exists()
