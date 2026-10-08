from django.urls import path, include
from django.http import JsonResponse
from accounts.security.sso.sso_view import GoogleLoginView, GoogleCallbackView
from accounts.security.mfa.mfa_view import MfaView


def health_check(request):
    return JsonResponse({"status": "UP"})


urlpatterns = [
    path('health/', health_check),
    path('api/gym/users/', include('users.urls')),
    path('api/gym/plans/', include('plans.urls')),
    path('api/gym/subscriptions/', include('subscriptions.urls')),
    path('api/gym/trainers/', include('trainers.urls')),
    path('api/gym/exercises/', include('exercises.urls')),
    path('api/gym/auth/google/', GoogleLoginView.as_view()),
    path('api/gym/auth/google/callback/', GoogleCallbackView.as_view()),
    path('api/gym/auth/mfa/verify/', MfaView.as_view()),
]
