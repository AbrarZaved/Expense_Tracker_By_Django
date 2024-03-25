from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm
from .models import Add_Expense
# Create your views here.
@login_required(login_url='/authentication/')
def index(request):
    data = Add_Expense.objects.all()
    return render(request, 'expenses/index.html', {'data': data})

def add_expense(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'expenses/add_expense.html', {'form': form})
    return render(request, 'expenses/add_expense.html', {'form': form})