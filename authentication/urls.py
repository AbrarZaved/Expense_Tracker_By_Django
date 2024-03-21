from django.contrib import admin
from django.urls import path
from .views import LoginView, UsernameValidationView, RegisterView, EmailValidationView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('login', LoginView.as_view(), name='login'), 
    path('validate_username', csrf_exempt(UsernameValidationView.as_view()), name='validate_username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('register', RegisterView.as_view(), name='register'), 
]
