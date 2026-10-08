from django.utils import timezone
from datetime import timedelta

from accounts.security.sso.google_provider import get_google_user_info
from accounts.security.email.email_service import generate_otp, send_otp_email
from accounts.security.auth.jwt_handler import generate_token
from accounts.security.otp.otp_purpose import OtpPurpose
from accounts.security.otp import otp_repository
from accounts.models import UserRolePermission
from users.repository import user_repository, user_tenant_repository


def google_sso_login(code: str) -> dict:
    user_info = get_google_user_info(code)

    email = user_info.get("email")
    name = user_info.get("name", "")

    if not email:
        raise ValueError("Email not found from Google")

    user = user_repository.find_by_email(email)
    if not user:
        raise ValueError("You are not registered. Contact admin.")

    if not user.tenant_id:
        raise ValueError("No tenant assigned. Contact admin.")

    user_tenant = user_tenant_repository.find_by_tenant_id(user.tenant_id)
    if not user_tenant:
        raise ValueError("Tenant not found. Contact admin.")

    if user_tenant.tfa_email:
        otp = generate_otp()
        otp_expiry = timezone.now() + timedelta(minutes=5)
        otp_repository.save(user.id, otp, otp_expiry, OtpPurpose.LOGIN)
        otp_repository.reset_attempts(user.id, OtpPurpose.LOGIN)
        send_otp_email(user.email, otp, user.name)
        return {"user_id": user.id, "message": "OTP sent to your email"}

    role_permissions = UserRolePermission.objects.filter(user_id=user.id)
    role = role_permissions.first().role if role_permissions.exists() else None
    permissions = list(role_permissions.values_list("permission", flat=True))
    token = generate_token(user.username, user.id, user.tenant_id)
    return {"message": "Login successful", "token": token, "role": role, "permissions": permissions}
