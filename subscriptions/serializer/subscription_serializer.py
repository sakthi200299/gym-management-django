from rest_framework import serializers
from subscriptions.model.subscription import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField(source='user.id', read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    plan_name = serializers.CharField(source='plan.name', read_only=True)
    plan_price = serializers.DecimalField(source='plan.price', max_digits=8, decimal_places=2, read_only=True)
    plan_duration = serializers.CharField(source='plan.duration', read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'user_id', 'plan', 'user_name', 'user_email', 'plan_name', 'plan_price', 'plan_duration', 'start_date', 'end_date', 'status']
        read_only_fields = ['id', 'user_id', 'user_name', 'user_email', 'plan_name', 'plan_price', 'plan_duration']
        extra_kwargs = {
            'user': {'write_only': True},
            'plan': {'write_only': True},
        }
