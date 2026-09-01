from django.db import models
from users.model.user import User
from plans.model.plan import Plan


class Subscription(models.Model):
    STATUS_CHOICES = [('active', 'Active'), ('inactive', 'Inactive')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='subscriptions')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    class Meta:
        app_label = 'subscriptions'

    def __str__(self):
        return f"{self.user.name} - {self.plan.name}"
