from django.urls import path
from exercises.controller.exercise_view import ExerciseView, ExerciseDetailView

urlpatterns = [
    path("", ExerciseView.as_view()),
    path("<int:exercise_id>/", ExerciseDetailView.as_view()),
]
