from django.shortcuts import render

from rest_framework import viewsets
from apps.assesment.models import Avalability
from apps.assesment.serializers import AvalabilitySerializer
from rest_framework import permissions


# Create your views here.

class AvalabilityViewSet(viewsets.ModelViewSet):
    queryset = Avalability.objects.all()
    serializer_class = AvalabilitySerializer
    permission_classes = [permissions.IsAuthenticated]
