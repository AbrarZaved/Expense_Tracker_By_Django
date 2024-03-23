
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('settings', views.setting, name='general_settings'),
    
]
