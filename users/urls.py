from django.urls import path
from users.controller.user_view import UserView, UserDetailView, ResetPasswordView
from accounts.security.auth.auth_view import AuthView

urlpatterns = [
    path("", UserView.as_view()),
    path("<int:user_id>/", UserDetailView.as_view()),
    path("login/", AuthView.as_view()),
    path("reset-password/", ResetPasswordView.as_view()),
]
