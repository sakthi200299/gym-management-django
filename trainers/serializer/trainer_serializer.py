from rest_framework import serializers
from trainers.model.trainer import Trainer


class TrainerSerializer(serializers.ModelSerializer):

    name = serializers.CharField(min_length=2)
    phone = serializers.CharField(min_length=10)
    specialization = serializers.CharField(min_length=2)
    experience_years = serializers.IntegerField(min_value=0, max_value=50)

    class Meta:
        model = Trainer
        fields = ['id', 'name', 'email', 'phone', 'specialization', 'experience_years']
        read_only_fields = ['id']
