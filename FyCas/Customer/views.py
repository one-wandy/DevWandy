from django.shortcuts import render
from django.views.generic import *
from . import forms
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .mixing import *
import os
from datetime import datetime
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
        cu = self.model.objects.all()
        for c in cu:
            print(c.credit.all())
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
        customer.name_r1 = request.POST.get("name_r1")
        customer.number_r1 = int(request.POST.get("number_r1"))
        customer.name_r2 = request.POST.get("name_r1")
        customer.number_r2 = int(request.POST.get("number_r2"))

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
        
        context['mont'] = self.MontNow(datetime.now().month)
        context['day'] = self.DayNow(datetime.now().day)
        context['day_number'] = datetime.now().day
        context['year'] = self.YearNow(datetime.now().year)
        context['year_number'] = datetime.now().year
        customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        try:
            credit = models.Credit.objects.get(customer=customer) 
            context["credit"] = credit
            context["amount"] = self.Amount(credit.amount)
        except models.Credit.DoesNotExist:
            return redirect(reverse('customer:create-credit'))
        return context
    
class NotaryCustomer(UpdateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/notary-customer.html"
    
    def get_context_data(self, **kwargs):
        year = {
        2023: "dos mil veintitrés",
        2024: "dos mil veinticuatro",
        2025: "dos mil veinticinco",
        2026: "dos mil veintiséis",
        2027: "dos mil veintisiete",
        2028: "dos mil veintiocho",
        2029: "dos mil veintinueve",
        2030: "dos mil treinta",
        2031: "dos mil treinta y uno",
        2032: "dos mil treinta y dos",
        2033: "dos mil treinta y tres",
        2034: "dos mil treinta y cuatro",
        2035: "dos mil treinta y cinco",
        2036: "dos mil treinta y seis",
        2037: "dos mil treinta y siete",
        2038: "dos mil treinta y ocho",
        2039: "dos mil treinta y nueve",
        2040: "dos mil cuarenta"
    }
        day = {
        1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
        6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez",
        11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
        16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve", 20: "veinte",
        21: "veintiuno", 22: "veintidós", 23: "veintitrés", 24: "veinticuatro", 25: "veinticinco",
        26: "veintiséis", 27: "veintisiete", 28: "veintiocho", 29: "veintinueve", 30: "treinta",
        31: "treinta y uno"
    }
        mont = {
        1: "enero",     2: "febrero",   3: "marzo",    4: "abril", 5: "mayo",
        6: "junio", 7: "julio", 8: "agosto",    9: "septiembre",
        10: "octubre",  11: "noviembre",  12: "diciembre"
        }
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['mont'] = mont.get(datetime.now().month)
        context['day'] = datetime.now().day
        context['day_number'] = day.get(datetime.now().day)
        context['year'] = year.get(datetime.now().year)
        context['year_number'] = datetime.now().year


        
        return context
    
    
    
class CreateCredit(CreateView, Options):
    model = models.Credit
    form_class = forms.CreditForm
    template_name = "customer/create-credit.html"

    def get(self, request, *args, **kwargs):
        customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
        try:
            credit = self.model.objects.get(customer=customer)
            return self.UpdateCredit(credit.id)
        except self.model.DoesNotExist:
            return super().get(request, *args, **kwargs)
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
        context['c'] = customer
        return context
    
    def post(self, request, *args, **kwargs):
        f = self.form_class(request.POST)
        if f.is_valid():
            credit = f.save()
            credit.customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
            credit.save()
        return self.List_Redirect()
    
    
class UpdateCredit(UpdateView, Options):
    model = models.Credit
    form_class = forms.CreditForm
    template_name = "customer/update-credit.html"
    
                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        credit =  self.model.objects.get(id=self.kwargs.get('pk'))
        context['c'] = models.Customer.objects.get(id=credit.customer.id)
        return context
    
    
    
    def post(self, request, *args, **kwargs):        
        credit = self.model.objects.get(id=self.kwargs.get('pk'))
        credit.customer = models.Customer.objects.get(id=credit.customer.id)
        credit.name = request.POST.get("name")
        credit.dni = request.POST.get("dni")
        credit.price_feed = request.POST.get("price_feed")
        credit.day_pay = request.POST.get("day_pay")
        credit.amount = request.POST.get("amount")
        credit.no_account = request.POST.get("no_account")
        credit.amount_feed = request.POST.get("amount_feed")
        credit.mode_pay = True if request.POST.get("mode_pay") == "on" else False
        credit.save()
        return self.List_Redirect()
