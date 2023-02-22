from django.shortcuts import render
from .models import Avalability
from .serializers import AvalabilitySerializer
from rest_framework import viewsets


# Create your views here.
class AvalabilityViewSet(viewsets.ModelViewSet):
    queryset = Avalability.objects.all()
    serializer_class = AvalabilitySerializer
