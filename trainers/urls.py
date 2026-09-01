from django.urls import path
from trainers.controller.trainer_controller import TrainerController, TrainerDetailController

urlpatterns = [
    path("", TrainerController.as_view()),
    path("<int:trainer_id>/", TrainerDetailController.as_view()),
]
