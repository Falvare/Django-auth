from django.urls import path
from .views import register, success

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profiles/', success, name='success')
]
