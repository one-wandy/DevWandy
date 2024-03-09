from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
      path('add-customer', views.AddCustomer.as_view(), name='add-customer'),
       path('list-customer', views.ListCustomer.as_view(), name='list-customer'),
]
