from django.contrib import admin
from django.urls import path
from .views import LoginView, UsernameValidationView, RegisterView, EmailValidationView, LogoutView, LoginAuthView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('login', LoginView.as_view(), name='login_page'), 
    path('validate_username', csrf_exempt(UsernameValidationView.as_view()), name='validate_username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login_auth', LoginAuthView.as_view(), name='login'),
]
