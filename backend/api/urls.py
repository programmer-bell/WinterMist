# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),  # /api/
    path('all/', views.all_api),  # /api/all/
]
