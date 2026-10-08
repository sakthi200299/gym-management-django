from rest_framework import serializers
from plans.model.plan import Plan


class PlanSerializer(serializers.ModelSerializer):

    name = serializers.CharField(min_length=2)
    price = serializers.DecimalField(max_digits=8, decimal_places=2, min_value=0)
    duration = serializers.CharField(min_length=2)

    class Meta:
        model = Plan
        fields = ['id', 'name', 'price', 'duration', 'description']
        read_only_fields = ['id']
