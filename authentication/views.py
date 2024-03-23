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
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out')
        return render(request, 'authentication/sign_in.html')

class LoginAuthView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'expenses/index.html')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'authentication/sign_in.html')