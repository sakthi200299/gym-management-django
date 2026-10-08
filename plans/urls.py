from django.urls import path
from plans.controller.plan_view import PlanView, PlanDetailView

urlpatterns = [
    path("", PlanView.as_view()),
    path("<int:plan_id>/", PlanDetailView.as_view()),
]
