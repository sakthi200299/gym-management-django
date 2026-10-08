from rest_framework import serializers
from exercises.model.exercise import Exercise


class ExerciseSerializer(serializers.ModelSerializer):

    trainer_name = serializers.CharField(source='trainer.name', read_only=True)
    subscription_status = serializers.CharField(source='subscription.status', read_only=True)
    name = serializers.CharField(min_length=2)
    category = serializers.CharField(min_length=2)
    sets = serializers.IntegerField(min_value=1, max_value=100)
    reps = serializers.IntegerField(min_value=1, max_value=100)
    duration_minutes = serializers.IntegerField(min_value=1, max_value=300)

    class Meta:
        model = Exercise
        fields = ['id', 'name', 'category', 'sets', 'reps', 'duration_minutes', 'trainer', 'trainer_name', 'subscription', 'subscription_status']
        read_only_fields = ['id', 'trainer_name', 'subscription_status']
        extra_kwargs = {
            'trainer':      {'write_only': True},
            'subscription': {'write_only': True},
        }
