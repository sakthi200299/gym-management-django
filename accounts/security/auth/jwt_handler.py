import jwt
from datetime import datetime, timezone, timedelta
from django.conf import settings

JWT_ALGORITHM = "HS256"
JWT_EXPIRY_HOURS = 1


def generate_token(username: str, user_id: int, tenant_id: str) -> str:
    payload = {
        "sub": username,
        "user_id": user_id,
        "tenant_id": tenant_id,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRY_HOURS),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=JWT_ALGORITHM)


def validate_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
