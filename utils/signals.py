from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.model.user import User
from config.cache_service import evict_permissions_cache


@receiver(post_save, sender=User)
def on_user_saved(sender, instance, created, **kwargs):
    if created:
        from accounts.security.email.email_service import generate_otp, send_otp_email
        from accounts.security.otp import otp_repository
        from accounts.security.otp.otp_purpose import OtpPurpose
        from django.utils import timezone
        from datetime import timedelta
        otp = generate_otp()
        otp_expiry = timezone.now() + timedelta(minutes=5)
        otp_repository.save(instance.id, otp, otp_expiry, OtpPurpose.LOGIN)
        send_otp_email.delay(instance.email, otp, instance.name)


@receiver(post_delete, sender=User)
def on_user_deleted(sender, instance, **kwargs):
    evict_permissions_cache(instance.id)
