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
    if request.method == 'POST':
        selected_currency = request.POST['currency']
        UserPreferences.objects.update_or_create(user=request.user, defaults={'currency': selected_currency})
        messages.success(request, 'Changes saved')
    return render(request, 'preferences/index.html', {'currency': currency})
