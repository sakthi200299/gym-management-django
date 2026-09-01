from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        app_label = 'plans'

    def __str__(self):
        return self.name
