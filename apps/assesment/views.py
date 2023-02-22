from django.shortcuts import render
from rest_framework import viewsets
from .models import Avalability
from .serializers import AvalabilitySerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def avalability_list(request):
    """
    List all avalability, or create a new avalability.
    """
    if request.method == 'GET':
        avalability = Avalability.objects.all()
        serializer = AvalabilitySerializer(avalability, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AvalabilitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def avalability_detail(request, pk):
    """
    Retrieve, update or delete a avalability.
    """
    try:
        avalability = Avalability.objects.get(pk=pk)
    except Avalability.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AvalabilitySerializer(avalability)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AvalabilitySerializer(avalability, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        avalability.delete()
        return HttpResponse(status=204)
