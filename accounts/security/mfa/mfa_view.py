from rest_framework.views import APIView
from rest_framework.exceptions import Throttled
from accounts.security.mfa.mfa_service import verify_otp
from accounts.security.mfa.mfa_serializer import VerifyOtpSerializer
from accounts.security.otp import otp_repository
from accounts.security.otp.otp_purpose import OtpPurpose
from config.api_response import success, error


class MfaView(APIView):
    throttle_scope = 'otp_verify'

    def post(self, request):
        try:
            serializer = VerifyOtpSerializer(data=request.data)
            if not serializer.is_valid():
                return error(message=serializer.errors, status_code=400)
            user_id = serializer.validated_data['user_id']
            otp_repository.check_rate_limit(user_id, OtpPurpose.LOGIN)
            result = verify_otp(serializer.validated_data)
            otp_repository.reset_attempts(user_id, OtpPurpose.LOGIN)
            return success(data=result, message="Login successful")
        except Throttled:
            raise
        except ValueError as e:
            user_id = request.data.get('user_id')
            if user_id:
                otp_repository.increment_attempts(user_id, OtpPurpose.LOGIN)
            return error(message=str(e), status_code=401)
        except Exception:
            return error(message="Internal server error", status_code=500)
