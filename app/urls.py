from django.urls import path
from . import views

urlpatterns = [
  # /app/
  path('', views.home, name='home'),
  
  # /app/login/
  path('login/', views.login, name='login'),
  
  # /app/signup/
  path('signup/', views.signup, name='signup')
]