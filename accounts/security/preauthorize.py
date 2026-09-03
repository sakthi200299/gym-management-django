from django.http import JsonResponse
from accounts.models import UserRolePermission


def preauthorize(permission: str):
    def decorator(view_func):
        def wrapper(self, request, *args, **kwargs):
            user_id = getattr(request, "auth_user", {}).get("user_id")
            if not user_id:
                return JsonResponse({"error": "Unauthorized"}, status=401)
            has_permission = UserRolePermission.objects.filter(
                user_id=user_id,
                permission=permission
            ).exists()
            if not has_permission:
                return JsonResponse({"error": "Access denied"}, status=403)
            return view_func(self, request, *args, **kwargs)
        return wrapper
    return decorator
