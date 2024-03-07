from django.shortcuts import render
from django.views.generic import ListView, View, CreateView
from . import forms
from . import models
class AddCustomer(CreateView):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/add-customer.html"