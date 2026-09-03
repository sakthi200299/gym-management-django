from django.http import JsonResponse
from django.views import View
from accounts.security import auth_service
from config.utils import json_body


class AuthController(View):

    def post(self, request):
        try:
            data = json_body(request)
            result = auth_service.login(
                data.get("username", "").strip(),
                data.get("password", "").strip()
            )
            return JsonResponse(result)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=401)
