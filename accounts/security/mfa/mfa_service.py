from django.utils import timezone

from accounts.security.auth.jwt_handler import generate_token
from accounts.security.otp.otp_purpose import OtpPurpose
from accounts.security.otp import otp_repository
from accounts.models import UserRolePermission
from users.repository import user_repository


def verify_otp(data: dict) -> dict:
    user_id = data['user_id']
    otp = data['otp']

    user = user_repository.find_by_id(user_id)
    if not user:
        raise ValueError("User not found")

    otp_record = otp_repository.find_by_user_and_purpose(user_id, OtpPurpose.LOGIN)
    if not otp_record or not otp_record.is_verified:
        raise ValueError("OTP is not valid")
    if otp_record.otp != otp:
        raise ValueError("Invalid OTP")
    if timezone.now() > otp_record.otp_expiry:
        raise ValueError("OTP expired")

    otp_repository.clear_otp(user_id, OtpPurpose.LOGIN)

    role_permissions = UserRolePermission.objects.filter(user_id=user.id)
    role = role_permissions.first().role if role_permissions.exists() else None
    permissions = list(role_permissions.values_list("permission", flat=True))

    token = generate_token(user.username, user.id, user.tenant_id)
    return {"token": token, "role": role, "permissions": permissions}
