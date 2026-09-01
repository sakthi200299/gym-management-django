from django.urls import path
from plans.controller.plan_controller import PlanController, PlanDetailController

urlpatterns = [
    path("", PlanController.as_view()),
    path("<int:plan_id>/", PlanDetailController.as_view()),
]
