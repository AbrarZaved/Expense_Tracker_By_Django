from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

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
    
    def post(self,request):
        #Get user data
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            
            #Validation
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, email=email)
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'Account successfully created')
                    return render(request, 'authentication/sign_up.html')
        return render(request, 'authentication/sign_up.html')
    