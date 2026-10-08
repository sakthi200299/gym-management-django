from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=3)
    password = serializers.CharField(required=True, write_only=True, min_length=10)
