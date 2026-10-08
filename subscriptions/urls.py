from django.urls import path
from subscriptions.controller.subscription_view import SubscriptionView, SubscriptionDetailView

urlpatterns = [
    path("", SubscriptionView.as_view()),
    path("<int:sub_id>/", SubscriptionDetailView.as_view()),
]
