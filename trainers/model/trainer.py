from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=50)
    experience_years = models.IntegerField()

    class Meta:
        app_label = 'trainers'

    def __str__(self):
        return self.name
