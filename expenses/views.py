from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm
from .models import Add_Expense
from django.contrib import messages as message
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url='/authentication/')
def index(request):
    
    data = Add_Expense.objects.all()
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'expenses/index.html', {'data': data, 'page_obj': page_obj})

def add_expense(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'expenses/add_expense.html', {'form': form})
    return render(request, 'expenses/add_expense.html', {'form': form})

def delete_expense(request, id):
    data = Add_Expense.objects.get(pk=id)
    data.delete()
    message.success(request, 'Expense deleted successfully')
    return redirect('index')

def edit_expense(request, id):
    data = Add_Expense.objects.get(pk=id)
    form = ExpenseForm(instance=data)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            message.success(request, 'Expense updated successfully')
            return redirect('index')
    return render(request, 'expenses/edit_expense.html', {'form': form})