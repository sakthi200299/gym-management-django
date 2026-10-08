from rest_framework import serializers


class VerifyOtpSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True, min_value=1)
    otp = serializers.CharField(required=True, min_length=6, max_length=6)
