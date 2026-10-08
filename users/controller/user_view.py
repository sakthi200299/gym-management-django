from rest_framework.views import APIView
from rest_framework.exceptions import Throttled
from users.service import user_service
from users.serializer.user_serializer import UserSerializer, ResetPasswordSerializer
from accounts.security.permission.preauthorize import preauthorize
from accounts.security.otp import otp_repository
from accounts.security.otp.otp_purpose import OtpPurpose
from config.api_response import success, error


class UserView(APIView):

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            user = user_service.register_user(serializer.validated_data)
            return success(data={"user": user}, message="User registered successfully", status_code=201)
        except ValueError as e:
            return error(message=str(e), status_code=409)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("GET_ALL_USERS")
    def get(self, request):
        try:
            users = user_service.get_all_users()
            return success(data={"users": users}, message="Users fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)


class ResetPasswordView(APIView):

    def post(self, request):
        try:
            serializer = ResetPasswordSerializer(data=request.data)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            user_id = serializer.validated_data['user_id']
            otp_repository.check_rate_limit(user_id, OtpPurpose.LOGIN)
            result = user_service.reset_password(serializer.validated_data)
            otp_repository.increment_attempts(user_id, OtpPurpose.LOGIN)
            return success(message=result['message'])
        except Throttled:
            raise
        except ValueError as e:
            user_id = request.data.get('user_id')
            if user_id:
                otp_repository.increment_attempts(user_id, OtpPurpose.LOGIN)
            return error(message=str(e), status_code=400)
        except Exception:
            return error(message="Internal server error", status_code=500)


class UserDetailView(APIView):

    @preauthorize("GET_USER_BY_ID")
    def get(self, request, user_id):
        try:
            user = user_service.get_user_by_id(user_id)
            return success(data={"user": user}, message="User fetched successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)

    @preauthorize("UPDATE_USER")
    def put(self, request, user_id):
        try:
            serializer = UserSerializer(data=request.data, partial=True)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            user = user_service.update_user(user_id, serializer.validated_data)
            return success(data={"user": user}, message="User updated successfully")
        except ValueError as e:
            return error(message=str(e), status_code=404)
        except Exception:
            return error(message="Internal server error", status_code=500)
