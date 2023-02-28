from rest_framework import serializers
from apps.assesment.models import Avalability


class AvalabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Avalability
        fields = '__all__'
