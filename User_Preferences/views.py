from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserPreferences
from django.contrib import messages
# Create your views here.
def setting(request):
    currency = []
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
    open(file_path, 'r')
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            currency.append({'name': key, 'value': value})
    existing_user_preferences = UserPreferences.objects.filter(user=request.user)
    if existing_user_preferences.exists():
        user_preferences = UserPreferences.objects.get(user=request.user)
    user_preferences = UserPreferences.objects.get(user=request.user)  
    if request.method=='POST':
        selected_currency = request.POST['currency']
        if existing_user_preferences.exists():
            user_preferences.currency = selected_currency
            user_preferences.save()  
        else:           
            UserPreferences.objects.create(user=request.user, currency=request.POST['currency'])
        messages.success(request, 'Changes saved successfully')
        return render(request, 'preferences/index.html', {'currency': currency, 'user_preferences': user_preferences})
        
    return render(request, 'preferences/index.html', {'currency': currency, 'user_preferences': user_preferences})
    