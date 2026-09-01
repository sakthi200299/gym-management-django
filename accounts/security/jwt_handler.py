import jwt
from datetime import datetime, timezone, timedelta
from django.conf import settings

JWT_ALGORITHM = "HS256"
JWT_EXPIRY_HOURS = 1


def generate_token(username: str) -> str:
    """
    Equivalent to JwtUtil.generateToken() in Spring Boot.
    Creates a signed JWT with subject and expiry.
    """
    payload = {
        "sub": username,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRY_HOURS),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=JWT_ALGORITHM)


def validate_token(token: str) -> dict:
    """
    Equivalent to JwtUtil.validateToken() in Spring Boot.
    Returns the decoded payload or raises ValueError.
    """
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")


def extract_username(token: str) -> str:
    """
    Equivalent to JwtUtil.extractUsername() in Spring Boot.
    """
    payload = validate_token(token)
    return payload["sub"]
