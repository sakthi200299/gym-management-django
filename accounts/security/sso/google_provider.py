from urllib.parse import urlencode
import requests
from django.conf import settings

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"
REDIRECT_URI = "http://localhost:8000/api/gym/auth/google/callback/"


def get_google_auth_url() -> str:
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
    }
    return f"{GOOGLE_AUTH_URL}?{urlencode(params)}"


def get_google_user_info(code: str) -> dict:
    token_response = requests.post(GOOGLE_TOKEN_URL, data={
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }, timeout=10)

    if token_response.status_code != 200:
        raise ValueError("Failed to fetch Google token")

    access_token = token_response.json().get("access_token")

    user_response = requests.get(GOOGLE_USERINFO_URL, headers={
        "Authorization": f"Bearer {access_token}"
    }, timeout=10)

    if user_response.status_code != 200:
        raise ValueError("Failed to fetch Google user info")

    return user_response.json()
