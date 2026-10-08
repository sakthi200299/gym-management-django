from django.db import models


class UserRolePermission(models.Model):
    user_id = models.IntegerField()
    role = models.CharField(max_length=50)
    permission = models.CharField(max_length=100)

    class Meta:
        app_label = 'accounts'

    def __str__(self):
        return f"{self.user_id} - {self.role} - {self.permission}"


class OtpVerification(models.Model):
    user_id = models.IntegerField()
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expiry = models.DateTimeField(null=True, blank=True)
    purpose = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    failed_attempts = models.IntegerField(default=0)
    locked_until = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'accounts'

    def __str__(self):
        return f"{self.user_id} - {self.purpose}"
