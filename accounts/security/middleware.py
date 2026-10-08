from django.http import JsonResponse
from accounts.security.auth.jwt_handler import validate_token

PUBLIC_ROUTES = {
    "/api/gym/users/": ["POST"],
    "/api/gym/users/login/": ["POST"],
    "/api/gym/auth/google/": ["GET"],
    "/api/gym/auth/google/callback/": ["GET"],
    "/api/gym/auth/mfa/verify/": ["POST"],
    "/health/": ["GET"],
}


class AuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.csrf_processing_done = True
        request.auth_user = None

        if request.path.startswith('/ws/'):
            return self.get_response(request)

        if self._is_public_route(request.path, request.method):
            return self.get_response(request)

        token = self._extract_token(request)
        if not token:
            return JsonResponse({"error": "Authorization header missing"}, status=401)

        try:
            payload = validate_token(token)
            request.auth_user = {
                "username": payload["sub"],
                "user_id": payload["user_id"],
                "tenant_id": payload.get("tenant_id"),
            }
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=401)

        return self.get_response(request)

    def _is_public_route(self, path, method):
        path = path if path.endswith("/") else f"{path}/"
        allowed_methods = PUBLIC_ROUTES.get(path)
        return allowed_methods and method in allowed_methods

    def _extract_token(self, request) -> str | None:
        header = request.headers.get("Authorization", "")
        if header.startswith("Bearer "):
            return header[7:]
        return None
