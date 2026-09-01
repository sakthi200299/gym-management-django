from django.urls import path
from exercises.controller.exercise_controller import ExerciseController, ExerciseDetailController

urlpatterns = [
    path("", ExerciseController.as_view()),
    path("<int:exercise_id>/", ExerciseDetailController.as_view()),
]
