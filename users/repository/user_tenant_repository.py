from users.model.user_tenant import UserTenant


def find_by_tenant_id(tenant_id: str) -> UserTenant | None:
    return UserTenant.objects.filter(tenant_id=tenant_id).first()
