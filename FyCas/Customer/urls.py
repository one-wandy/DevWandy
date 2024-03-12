from django.contrib import admin
from django.urls import path, include
from . import views, views_ajax

app_name = "customer"
urlpatterns = [
      path('add-customer', views.AddCustomer.as_view(), name='add-customer'),
      path('update-customer/<int:pk>', views.UpdateCustomer.as_view(), name='update-customer'),
      path('delete-customer/<int:pk>', views.DeleteCustomer.as_view(), name='delete-customer'),

      path('list-customer', views.ListCustomer.as_view(), name='list-customer'),
      path('card-customer/<int:pk>', views.CardCustomer.as_view(), name='card-customer'),
      path('notary-customer/<int:pk>', views.NotaryCustomer.as_view(), name='notary-customer'),


      # Views Ajax
      path("searching/customer", views_ajax.SearchCustomer, name="searching-customer"),

      
]
