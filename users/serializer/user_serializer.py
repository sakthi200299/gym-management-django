from rest_framework import serializers
from users.model.user import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, min_length=10)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'phone', 'age', 'gender', 'joined_date']
        read_only_fields = ['id', 'joined_date']
        extra_kwargs = {
            'password_hash': {'write_only': True},
        }


class ResetPasswordSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True, min_value=1)
    new_password = serializers.CharField(required=True, write_only=True, min_length=10)
