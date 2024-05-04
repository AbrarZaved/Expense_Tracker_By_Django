from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_expense', views.add_expense, name='expense'),
    path('delete_expense/<int:id>', views.delete_expense, name='delete'),
    path('edit_expense/<int:id>', views.edit_expense, name='edit'),
    path('search_expenses', csrf_exempt(views.search_expense), name='search_expenses'),
    path('all_expenses', views.all_expenses, name='all_expenses'),
    path('stat', views.stats_view, name='stat'),
    path('expense_category_summary', views.expense_category_summary, name='expense_category_summary'),
]
