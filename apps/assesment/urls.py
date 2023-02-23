from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.assesment.views import AvalabilityViewSet

router = DefaultRouter()
router.register('avalability', AvalabilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
