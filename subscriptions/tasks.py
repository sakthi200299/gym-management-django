from celery import shared_task
from django.utils import timezone
from django.conf import settings
from datetime import timedelta


@shared_task
def send_expiry_reminder():
    from subscriptions.model.subscription import Subscription
    from django.core.mail import send_mail
    from django.conf import settings

    today = timezone.now().date()
    reminder_date = today + timedelta(weeks=1)
    expiring = Subscription.objects.filter(
        end_date__lte=reminder_date,
        end_date__gte=today,
        status='active'
    ).select_related('user', 'plan')

    for sub in expiring:
        send_mail(
            subject="Subscription Expiry Reminder",
            message=(
                f"Hi {sub.user.name},\n\n"
                f"Your {sub.plan.name} subscription expires on {sub.end_date}.\n"
                f"Renew now to avoid interruption."
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.user.email],
            fail_silently=False,
        )
