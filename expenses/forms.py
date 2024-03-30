from django.forms import ModelForm
from django import forms

from .models import Add_Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Add_Expense
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'currency': forms.Select(attrs={'class': 'form-control'}),      
        }
        
    
    