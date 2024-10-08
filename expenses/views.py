from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm
from .models import Add_expense
from django.contrib import messages as message
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from User_Preferences.models import UserPreferences
import datetime
# Create your views here.


def search_expense(request):
    if request.method == 'POST':
        search = json.loads(request.body).get('searchText')
        expenses = Add_expense.objects.filter(amount__icontains=search, user=request.user) | Add_expense.objects.filter(category__icontains=search, user=request.user) | Add_expense.objects.filter(date__icontains=search, user=request.user) | Add_expense.objects.filter(description__icontains=search, user=request.user)
        data = expenses.values()
        return JsonResponse(list(data), safe=False)

def all_expenses(request):
    data = Add_expense.objects.filter(user=request.user)
    currency = UserPreferences.objects.get(user=request.user).currency
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'expenses/all_expenses.html', {'data': data, 'page_obj': page_obj, 'currency': currency})

@login_required(login_url='/authentication/')
def index(request):
    data = Add_expense.objects.filter(user=request.user)
    currency = UserPreferences.objects.all()
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'expenses/index.html', {'data': data, 'page_obj': page_obj, 'currency': currency})   

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)  
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            message.success(request, 'Expense added successfully') 
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request, id):
    data = Add_expense.objects.get(pk=id)
    data.delete()
    message.success(request, 'Expense deleted successfully')
    return redirect('index')

def edit_expense(request, id):
    data = Add_expense.objects.get(pk=id)
    form = ExpenseForm(instance=data)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            message.success(request, 'Expense updated successfully')
            return redirect('index')
    return render(request, 'expenses/edit_expense.html', {'form': form})




def expense_category_summary(request):
    today = datetime.date.today()
    six_months_ago = today - datetime.timedelta(days=30*6)
    expenses = Add_expense.objects.filter(user=request.user, date__gte=six_months_ago, date__lte=today)
    
    finalrep = {}

    def get_category_amount(category):
        filtered_by_category = expenses.filter(category=category)
        amount = sum(item.amount for item in filtered_by_category)
        return amount

    category_list = set(expense.category for expense in expenses)
    print(category_list)
    for category in category_list:
        finalrep[category] = get_category_amount(category)
    print(finalrep)
    return JsonResponse({'category_data': finalrep}, safe=False)

def stats_view(request):
    return render(request, 'expenses/stats.html')


