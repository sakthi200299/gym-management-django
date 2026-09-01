from django.db import models
from trainers.model.trainer import Trainer
from subscriptions.model.subscription import Subscription


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    sets = models.IntegerField()
    reps = models.IntegerField()
    duration_minutes = models.IntegerField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='exercises')
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='exercises')

    class Meta:
        app_label = 'exercises'

    def __str__(self):
        return self.name
