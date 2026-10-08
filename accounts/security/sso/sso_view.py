from urllib.parse import unquote
from django.http import HttpResponseRedirect
from rest_framework.views import APIView

from accounts.security.sso.google_provider import get_google_auth_url
from accounts.security.sso.sso_service import google_sso_login
from config.api_response import success, error


class GoogleLoginView(APIView):

    def get(self, request):
        return HttpResponseRedirect(get_google_auth_url())


class GoogleCallbackView(APIView):
    throttle_scope = 'sso'

    def get(self, request):
        try:
            code = unquote(request.GET.get("code", ""))
            if not code:
                return error(message="Authorization code missing", status_code=400)
            result = google_sso_login(code)
            return success(data=result, message=result.get("message", "Login successful"))
        except ValueError as e:
            return error(message=str(e), status_code=400)
        except Exception:
            return error(message="Internal server error", status_code=500)
