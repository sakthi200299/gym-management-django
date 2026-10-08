import random
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


def generate_otp() -> str:
    return str(random.randint(100000, 999999))


@shared_task
def send_otp_email(to_email: str, otp: str, username: str) -> None:
    send_mail(
        subject="Your Login OTP",
        message=(
            f"Hi {username},\n\n"
            f"Your OTP for login is: {otp}\n\n"
            f"This OTP is valid for 5 minutes.\n"
            f"Do not share this OTP with anyone."
        ),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False,
    )
