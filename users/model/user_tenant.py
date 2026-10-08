from django.db import models


class UserTenant(models.Model):
    tenant_id = models.CharField(max_length=50, unique=True)
    tfa_email = models.BooleanField(default=False)
    tfa_phone = models.BooleanField(default=False)

    class Meta:
        app_label = 'users'
        db_table = 'users_usertenant'

    def __str__(self):
        return self.tenant_id
