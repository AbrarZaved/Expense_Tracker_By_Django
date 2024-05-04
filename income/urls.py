from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('income', views.index, name='income'),
    path('add_income', views.add_income, name='add_income'),
    path('delete_income/<int:id>', views.delete_income, name='delete_income'),
    path('edit_income/<int:id>', views.edit_income, name='edit_income'),
    path('search_incomes', csrf_exempt(views.search_income), name='search_incomes'),
]
