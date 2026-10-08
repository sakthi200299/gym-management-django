from datetime import timedelta
from django.utils import timezone
from rest_framework.exceptions import Throttled
from accounts.models import OtpVerification

MAX_ATTEMPTS = 3
LOCKOUT_MINUTES = 2


def save(user_id: int, otp: str, otp_expiry, purpose: str) -> OtpVerification:
    record, _ = OtpVerification.objects.update_or_create(
        user_id=user_id, purpose=purpose,
        defaults={'otp': otp, 'otp_expiry': otp_expiry, 'is_verified': True}
    )
    return record


def find_by_user_and_purpose(user_id: int, purpose: str) -> OtpVerification | None:
    return OtpVerification.objects.filter(user_id=user_id, purpose=purpose).first()


def clear_otp(user_id: int, purpose: str) -> None:
    OtpVerification.objects.filter(user_id=user_id, purpose=purpose).update(is_verified=False)


def reset_attempts(user_id: int, purpose: str) -> None:
    OtpVerification.objects.filter(user_id=user_id, purpose=purpose).update(
        failed_attempts=0, locked_until=None
    )


def check_rate_limit(user_id: int, purpose: str) -> None:
    record = find_by_user_and_purpose(user_id, purpose)
    if not record:
        return
    if record.locked_until and timezone.now() < record.locked_until:
        wait = (record.locked_until - timezone.now()).seconds
        raise Throttled(wait=wait)
    if record.locked_until and timezone.now() >= record.locked_until:
        OtpVerification.objects.filter(user_id=user_id, purpose=purpose).update(
            failed_attempts=0, locked_until=None
        )


def increment_attempts(user_id: int, purpose: str) -> None:
    record, _ = OtpVerification.objects.get_or_create(
        user_id=user_id, purpose=purpose,
        defaults={'failed_attempts': 0}
    )
    if record.failed_attempts >= MAX_ATTEMPTS:
        return
    attempts = record.failed_attempts + 1
    if attempts >= MAX_ATTEMPTS:
        OtpVerification.objects.filter(user_id=user_id, purpose=purpose).update(
            failed_attempts=attempts,
            locked_until=timezone.now() + timedelta(minutes=LOCKOUT_MINUTES),
            is_verified=False
        )
    else:
        OtpVerification.objects.filter(user_id=user_id, purpose=purpose).update(
            failed_attempts=attempts
        )
