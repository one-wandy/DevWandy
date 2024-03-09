from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "customer"
urlpatterns = [
      path('add-customer', views.AddCustomer.as_view(), name='add-customer'),
      path('update-customer/<int:pk>', views.UpdateCustomer.as_view(), name='update-customer'),
      path('delete-customer/<int:pk>', views.DeleteCustomer.as_view(), name='delete-customer'),

      path('list-customer', views.ListCustomer.as_view(), name='list-customer'),
      
]
