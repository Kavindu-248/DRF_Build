from django.urls import path
from apps.assesment import views

urlpatterns = [
    path('avalability/', views.avalability_list),
    path('avalability/<int:pk>/', views.avalability_detail),
]
