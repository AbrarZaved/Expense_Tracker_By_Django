
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add_expense', views.add_expense, name='expense'),
    
]
