import statistics
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from apps.assesment.models import Avalability
from apps.assesment.serializers import AvalabilitySerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class AvalabilityViewSet(viewsets.ModelViewSet):
    queryset = Avalability.objects.all()
    serializer_class = AvalabilitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Avalability.objects.all()
        serializer = AvalabilitySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if 'doctor' not in request.data:
            # If not, set the default doctor instance ID
            request.data['doctor'] = 1  # ID of the default Doctor instance

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        queryset = Avalability.objects.all()
        avalability = get_object_or_404(queryset, pk=pk)
        serializer = AvalabilitySerializer(avalability)
        return Response(serializer.data)

    def update(self, request, pk=None):
        avalability = Avalability.objects.get(pk=pk)
        serializer = AvalabilitySerializer(avalability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        avalability = Avalability.objects.get(pk=pk)
        avalability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
