from django.urls import path
from . import views

urlpatterns = [
  # ex: /app/
  path('', views.home, name='home')
]