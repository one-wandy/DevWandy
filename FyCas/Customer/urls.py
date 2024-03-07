from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
      path('', views.AddCustomer.as_view(), name='add-customer')
]
