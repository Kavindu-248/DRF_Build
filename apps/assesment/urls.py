from django.urls import path
from .views import avalability_list, avalability_detail
from rest_framework.urlpatterns import format_suffix_patterns
from apps.assesment import views

urlpatterns = [
    path('avalability/', views.avalability_list.as_view()),
    path('avalability/<int:pk>/', views.avalability_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
