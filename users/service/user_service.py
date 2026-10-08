import hashlib

from django.db import transaction

from users.repository import user_repository
from users.serializer.user_serializer import UserSerializer
from accounts.security.otp import otp_repository
from accounts.security.otp.otp_purpose import OtpPurpose
from accounts.security.email.email_service import generate_otp, send_otp_email
from django.utils import timezone
from datetime import timedelta

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def _check_password(raw: str, hashed: str) -> bool:
    return _hash_password(raw) == hashed


@transaction.atomic
def register_user(data: dict) -> dict:
    if user_repository.exists_by_username(data.get("username")):
        raise ValueError("Username already exists")
    if user_repository.exists_by_email(data.get("email")):
        raise ValueError(f"Email '{data.get('email')}' already exists")
    password_hash = _hash_password(data.get("password"))
    user = user_repository.save({
        **{k: v for k, v in data.items() if k != 'password'},
        "password_hash": password_hash,
    })
    return UserSerializer(user).data


@transaction.atomic
def update_user(user_id: int, data: dict) -> dict:
    user = user_repository.find_by_id(user_id)
    if not user:
        raise ValueError(f"User with id {user_id} not found")
    user = user_repository.update(user, {k: v for k, v in data.items() if k != 'password'})
    return UserSerializer(user).data


def load_user(username: str, password: str) -> dict:
    user = user_repository.find_by_username(username)
    if not user or not _check_password(password, user.password_hash):
        raise ValueError("Invalid username or password")
    return {"id": user.id, "username": user.username, "email": user.email}


def get_all_users() -> list:
    users = user_repository.find_all_objects()
    if not users:
        raise ValueError("No users found")
    return UserSerializer(users, many=True).data


def get_user_by_id(user_id: int) -> dict:
    user = user_repository.find_by_id(user_id)
    if not user:
        raise ValueError(f"User with id {user_id} not found")
    return UserSerializer(user).data


def reset_password(data: dict) -> dict:
    user = user_repository.find_by_id(data['user_id'])
    if not user:
        raise ValueError("User not found")
    user_repository.update(user, {"password_hash": _hash_password(data['new_password'])})
    otp = generate_otp()
    otp_expiry = timezone.now() + timedelta(minutes=5)
    otp_repository.save(user.id, otp, otp_expiry, OtpPurpose.LOGIN)
    send_otp_email(user.email, otp, user.name)
    return {"message": "Password reset successful. OTP sent to your email."}
