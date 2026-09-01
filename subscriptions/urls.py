from django.urls import path
from subscriptions.controller.subscription_controller import SubscriptionController, SubscriptionDetailController

urlpatterns = [
    path("", SubscriptionController.as_view()),
    path("<int:sub_id>/", SubscriptionDetailController.as_view()),
]
