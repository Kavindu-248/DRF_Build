from django.shortcuts import render
from .models import Avalability
from .serializers import AvalabilitySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class avalability_list(APIView):
    """
    List all avalability, or create a new avalability.
    """

    def get(self, request, format=None):
        avalability = Avalability.objects.all()
        serializer = AvalabilitySerializer(avalability, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AvalabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class avalability_detail(APIView):
    """
    Retrieve, update or delete a avalability instance.
    """

    def get_object(self, pk):
        try:
            return Avalability.objects.get(pk=pk)
        except Avalability.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        avalability = self.get_object(pk)
        serializer = AvalabilitySerializer(avalability)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        avalability = self.get_object(pk)
        serializer = AvalabilitySerializer(avalability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        avalability = self.get_object(pk)
        avalability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
