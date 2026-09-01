import json
from django.http import JsonResponse
from .jwt_handler import validate_token, extract_username, generate_token

PUBLIC_ROUTES = [
    "/api/gym/users/",
]

LOGIN_ROUTE = "/api/gym/users/login/"


class JwtAuthFilter:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in PUBLIC_ROUTES and request.method == "POST":
            return self.get_response(request)

        if request.path == LOGIN_ROUTE and request.method == "POST":
            return self._handle_login(request)

        token = self._extract_token(request)
        if not token:
            return JsonResponse({"error": "Authorization header missing"}, status=401)

        try:
            username = extract_username(token)
            from users.service import user_service
            user = user_service.get_user_by_username(username)
            if not user:
                return JsonResponse({"error": "User not found"}, status=401)
            request.auth_user = user
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=401)

        return self.get_response(request)

    def _handle_login(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        if not username or not password:
            return JsonResponse({"error": "username and password are required"}, status=400)

        try:
            from users.service import user_service
            user = user_service.load_user(username, password)
            token = generate_token(user["username"])
            return JsonResponse({"token": token, "user": user})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=401)

    def _extract_token(self, request) -> str | None:
        header = request.headers.get("Authorization", "")
        if header.startswith("Bearer "):
            return header[7:]
        return None
