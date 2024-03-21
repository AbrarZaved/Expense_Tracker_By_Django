from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/sign_in.html')

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Username already exists'}, status=400)
        return JsonResponse({'username_valid': True})

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Email already exists'}, status=400)
        return JsonResponse({'email_valid': True})
    
   
class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/sign_up.html')