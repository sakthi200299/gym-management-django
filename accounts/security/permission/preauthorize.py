import functools

from django.http import JsonResponse
from accounts.models import UserRolePermission
from config.cache_service import get_cached_permissions, set_cached_permissions


def preauthorize(permission: str):
    def decorator(view_func):
        @functools.wraps(view_func)
        def wrapper(self, request, *args, **kwargs):
            user_id = getattr(request, "auth_user", {}).get("user_id")
            if not user_id:
                return JsonResponse({"error": "Unauthorized"}, status=401)

            cached = get_cached_permissions(user_id)        # L2 Redis check
            if cached is None:
                perms = UserRolePermission.objects.filter(user_id=user_id)
                cached = list(perms.values_list("permission", flat=True))
                set_cached_permissions(user_id, cached)     # store in Redis

            if permission not in cached:
                return JsonResponse({"error": "Access denied"}, status=403)
            return view_func(self, request, *args, **kwargs)
        return wrapper
    return decorator
