from django.shortcuts import render
from django.views.generic import *
from . import forms
from . import models
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .mixing import *
import os
class AddCustomer(CreateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/add-customer.html"
    
    def post(self, request, *args, **kwargs):
        f = self.form_class(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            # Creando Carpeta para el Cliente
            self.FileCreate(f.instance.name, f.instance.last_name)
        return self.List_Redirect()

# #Crear una funcion al crear clientes 
# import os
#path = os.getcwd() + "\Clientes"
# sub_file = "CARPS"
# sub_file = os.path.join(path, sub_file)
# try:
#     os.mkdir(sub_file)
#     print(f" '{sub_file}' Creada correctamente.")
# except FileExistsError:
#     print(f"'{sub_file}' Ya existe")


    
    def get_success_url(self):
        # Redirigir a una URL específica después de guardar el formulario
        return reverse_lazy('mi_vista_de_exito')
    
class ListCustomer(ListView):
    model = models.Customer
    template_name = "customer/list-customer.html"
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = self.model.objects.all().order_by('-id')
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
        customer.dni = int(request.POST.get("dni"))
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
    
class CardCustomer(UpdateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/card-customer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        return context
    
class NotaryCustomer(UpdateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/notary-customer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        return context
    
    