from rest_framework import serializers
from .models import Avalability


class AvalabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Avalability
        fields = '__all__'
