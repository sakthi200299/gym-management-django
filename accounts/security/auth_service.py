from accounts.security.jwt_handler import generate_token
from accounts.models import UserRolePermission


def login(username: str, password: str) -> dict:
    from users.service import user_service
    user = user_service.load_user(username, password)

    role_permissions = UserRolePermission.objects.filter(user_id=user["id"])
    role = role_permissions.first().role if role_permissions.exists() else None
    permissions = list(role_permissions.values_list("permission", flat=True))

    token = generate_token(user["username"], user["id"])
    return {
        "token": token,
        "role": role,
        "permissions": permissions
    }
