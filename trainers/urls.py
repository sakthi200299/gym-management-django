from django.urls import path
from trainers.controller.trainer_view import TrainerView, TrainerDetailView

urlpatterns = [
    path("", TrainerView.as_view()),
    path("<int:trainer_id>/", TrainerDetailView.as_view()),
]
