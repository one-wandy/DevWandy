from django.contrib import admin
from django.urls import path, include
from . import views, views_ajax

app_name = "customer"
urlpatterns = [
      path("", views.Dashboard.as_view(), name='dashboard'),
      path('add-customer', views.AddCustomer.as_view(), name='add-customer'),
      path('detail-customer/<int:pk>', views.DetailCustomer.as_view(), name='detail-customer'),
      path('update-customer/<int:pk>', views.UpdateCustomer.as_view(), name='update-customer'),
      
      path('delete-customer/<int:pk>', views.DeleteCustomer.as_view(), name='delete-customer'),

      path('list-customer', views.ListCustomer.as_view(), name='list-customer'),
      path('card-customer/<int:pk>/<int:credit_id>', views.CardCustomer.as_view(), name='card-customer'),
      path('notary-customer/<int:pk>/<int:notary_id>', views.NotaryCustomer.as_view(), name='notary-customer'),
      
      path('create-credit/<int:pk>', views.CreateCredit.as_view(), name='create-credit'),
      path('update-credit/<int:pk>', views.UpdateCredit.as_view(), name='update-credit'),
      path('list-credit/<int:pk>', views.ListCredit.as_view(), name='list-credit'),

      path("detail-credit/customer/<int:pk>", views.DetailCreditCustomer.as_view(), name="detail-credit-cutomer"),

      path("no-approved/customer", views.NoApproved.as_view(), name='no-approved'),
      path("approved/customer/<int:pk>", views.Approved.as_view(), name='approved'),
      path("create/customer-debit", views.CreateCustomerDebit.as_view(), name='create-customer-debit'),
      
      path("mensaje/customer-debit", views.MensajeCustomerDebit.as_view(), name='mensaje-customer-debit'),

      path("select/customer", views.ListCustomerSelect.as_view(), name='select-customer'),
      


      # Views Ajax
      path("searching/customer", views_ajax.SearchCustomer, name="searching-customer"),
      path("verify-false/customer/", views_ajax.CustomerVerifyTurnFalse, name="verify-false-customer"),

      path("turn-debit/customer/", views_ajax.TurnDebeit, name="turn-debit-customer"),
      path("turn-debit-follow/customer/", views_ajax.TurnDebeitFollow, name="turn-debit-customer-follow"),

      path("turn-debit-active/customer/", views_ajax.TurnDebeitActive, name="turn-debit-customer-active"),
      
]
