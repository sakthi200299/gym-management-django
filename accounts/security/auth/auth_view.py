from rest_framework.views import APIView
from accounts.security.auth.auth_service import login
from accounts.security.auth.auth_serializer import LoginSerializer
from config.api_response import success, error


class AuthView(APIView):
    throttle_scope = 'login'

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            result = login(serializer.validated_data)
            return success(data=result, message=result.get("message", "Login successful"))
        except ValueError as e:
            return error(message=str(e), status_code=401)
        except Exception:
            return error(message="Internal server error", status_code=500)
