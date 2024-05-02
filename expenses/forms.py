from django.forms import ModelForm
from django import forms

from .models import Add_expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Add_expense
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(), # This is a hidden input field, it is hidden from the user
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Amount', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),  
        }
        
    
    