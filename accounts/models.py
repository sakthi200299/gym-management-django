from django.db import models
from users.model.user import User


class UserRolePermission(models.Model):

    class Role(models.TextChoices):
        USER = "USER", "User"
        ADMIN = "ADMIN", "Admin"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='role_permissions', null=True)
    role = models.CharField(max_length=10, choices=Role.choices)
    permission = models.CharField(max_length=50)

    class Meta:
        app_label = 'accounts'
        unique_together = ('user', 'role', 'permission')

    def __str__(self):
        return f"{self.user_id} - {self.role} - {self.permission}"
