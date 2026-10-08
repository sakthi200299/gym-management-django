from django.utils import timezone
from datetime import timedelta

from accounts.security.email.email_service import generate_otp, send_otp_email
from accounts.security.auth.jwt_handler import generate_token
from accounts.security.otp.otp_purpose import OtpPurpose
from accounts.security.otp import otp_repository
from accounts.models import UserRolePermission
from users.repository import user_repository, user_tenant_repository


def login(data: dict) -> dict:
    from users.service import user_service

    username = data['username']
    password = data['password']

    db_user = user_repository.find_by_username(username)
    if not db_user:
        raise ValueError("Invalid username or password")

    if not db_user.tenant_id:
        raise ValueError("No tenant assigned. Contact admin.")

    user_service.load_user(username, password)

    user_tenant = user_tenant_repository.find_by_tenant_id(db_user.tenant_id)
    if not user_tenant:
        raise ValueError("Tenant not found. Contact admin.")

    if user_tenant.tfa_email:
        otp = generate_otp()
        otp_expiry = timezone.now() + timedelta(minutes=5)
        otp_repository.save(db_user.id, otp, otp_expiry, OtpPurpose.LOGIN)
        otp_repository.reset_attempts(db_user.id, OtpPurpose.LOGIN)
        send_otp_email(db_user.email, otp, db_user.name)
        return {"message": "OTP sent to your email", "user_id": db_user.id}

    role_permissions = UserRolePermission.objects.filter(user_id=db_user.id)
    role = role_permissions.first().role if role_permissions.exists() else None
    permissions = list(role_permissions.values_list("permission", flat=True))
    token = generate_token(db_user.username, db_user.id, db_user.tenant_id)
    return {"message": "Login successful", "token": token, "role": role, "permissions": permissions}
