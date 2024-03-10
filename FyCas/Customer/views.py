from django.shortcuts import render
from django.views.generic import *
from . import forms
from . import models
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .mixing import *

class AddCustomer(CreateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/add-customer.html"
    
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return self.List_Redirect()


    
    def get_success_url(self):
        # Redirigir a una URL específica después de guardar el formulario
        return reverse_lazy('mi_vista_de_exito')
    
class ListCustomer(ListView):
    model = models.Customer
    template_name = "customer/list-customer.html"
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = self.model.objects.all()
        return context
    
    
class UpdateCustomer(UpdateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/update-customer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        return context
    
    def post(self, request, *args, **kwargs):        
        customer = self.model.objects.get(id=self.kwargs.get('pk'))
        customer.name = request.POST.get("name")
        customer.last_name = request.POST.get("last_name")
        customer.dni = request.POST.get("dni")
        customer.number = request.POST.get("number")
        customer.address = request.POST.get("address")
        customer.work_information = request.POST.get("work_information")
        if request.FILES.get("img1"):
            customer.img1 = request.FILES.get("img1")
        if request.FILES.get("img2"):
            customer.img2 = request.FILES.get("img2")
        customer.save()
        return self.List_Redirect()
            
        print(form.errors) 


class DeleteCustomer(DeleteView, Options):
    model = models.Customer
    template_name = "customer/delete-customer.html"
    success_url = reverse_lazy('list-customer')
    
    def get(self, request, *args, **kwargs):
        customer = self.model.objects.get(pk=self.kwargs.get('pk'))
        customer.delete()
        return self.List_Redirect()
    
