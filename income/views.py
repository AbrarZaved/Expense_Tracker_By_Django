from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import IncomeForm
from .models import Add_income
from django.contrib import messages as message
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from User_Preferences.models import UserPreferences


@login_required(login_url='/authentication/')
def index(request):
    data = Add_income.objects.filter(user=request.user)
    currency = UserPreferences.objects.all()        
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'income/index.html', {'data': data, 'page_obj': page_obj, 'currency': currency})

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)  
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            message.success(request, 'Income added successfully') 
            return redirect('income')
    form = IncomeForm()
    return render(request, 'income/add_income.html', {'form': form})

def search_income(request):
    if request.method == 'POST':
        search = json.loads(request.body).get('searchText')
        income = Add_income.objects.filter(amount__icontains=search, user=request.user) | Add_income.objects.filter(source__icontains=search, user=request.user) | Add_income.objects.filter(date__icontains=search, user=request.user) | Add_income.objects.filter(description__icontains=search, user=request.user)
        data = income.values()
        return JsonResponse(list(data), safe=False)

def delete_income(request, id):
    data = Add_income.objects.get(pk=id)
    data.delete()
    message.success(request, 'Income deleted successfully')
    return redirect('income')

def edit_income(request, id):
    data = Add_income.objects.get(pk=id)
    form = IncomeForm(instance=data)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            message.success(request, 'Income updated successfully')
            return redirect('income')
    return render(request, 'income/edit_income.html', {'form': form})