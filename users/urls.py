from django.urls import path
from users.controller.user_controller import UserController, UserDetailController

urlpatterns = [
    path("", UserController.as_view()),
    path("<int:user_id>/", UserDetailController.as_view()),
    path("login/", UserController.as_view()),
]
