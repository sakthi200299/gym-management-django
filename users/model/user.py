from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, default='')
    password_hash = models.CharField(max_length=64, default='')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    joined_date = models.DateField(auto_now_add=True)
    tenant_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = 'users'
        ordering = ['-id']

    def __str__(self):
        return self.name
