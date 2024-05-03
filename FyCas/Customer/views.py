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



class Dashboard(TemplateView, Options):
    template_name = "base/dashboard.html"
    
    
    
    
class AddCustomer(CreateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/create-customer.html"
    
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = self.Setting()
        return context
    
    
    def post(self, request, *args, **kwargs):
        f = self.form_class(request.POST, request.FILES)
        if f.is_valid():
            if request.POST.get('sex-man') != 'man':
                f.sexo = 'F'
            f.instance.name = f.instance.name.title()
            f.instance.last_name = f.instance.last_name.title()
            # f.save()
            # Creando Carpeta para el Cliente
            self.FileCreate(f.instance.name, f.instance.last_name)
            return redirect(reverse('maps:maps-customer'))
        else:
            return redirect(reverse('customer:add-customer'))

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
        context['customer'] = self.model.objects.filter(is_active = True).order_by('-id')[:20]
        # cu = self.model.objects.all()
        return context
    
    
class UpdateCustomer(UpdateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/update-customer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['credit'] = models.Credit.objects.filter(customer__id=self.kwargs.get('pk'))
        return context
    
    def form_valid(self, form_class):
        form_class.save()
        return HttpResponseRedirect(reverse('customer:list-customer')) 
        # c.last_name = request.POST.get("last_name").title()
        # c.dni = request.POST.get("dni")
        # c.number = request.POST.get("number")
        # c.address = request.POST.get("address")
        # c.name_r1 = request.POST.get("name_r1")
        # c.number_r1 = request.POST.get("number_r1")
        # c.name_r2 = request.POST.get("name_r1")
        # c.number_r2 = request.POST.get("number_r2")

        # c.work_information = request.POST.get("work_information")
        # if request.FILES.get("img1"):
        #     c.img1 = request.FILES.get("img1")
        # if request.FILES.get("img2"):
        #     c.img2 = request.FILES.get("img2")
            
        


class DetailCustomer(DetailView, Options):
    model = models.Customer
    template_name = "customer/detail-customer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['credit'] = models.Credit.objects.filter(customer__id=self.kwargs.get('pk'))

        return context
    

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
    template_name = "customer/card-fycas.html"
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.model.objects.get(id=self.kwargs.get('pk')).company == "ThomFin Group":
            # Aquí puedes cambiar la plantilla si es necesario
            self.template_name = "base/dashboard.html"
        return super().get(request, *args, **kwargs)
    
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
            credit = models.Credit.objects.get(customer=customer, id=self.kwargs.get('credit_id')) 
            context["amount"] = self.Amount(credit.amount)
            context["day_pay"] = self.DayNow(credit.day_pay)

            context["credit"] = credit
            if credit.amount_feed:
                print(credit.amount_feed)
                v_amount = str(credit.amount_feed)
                # print(v_amount[:v_amount.index(".")])
                context["amount_feed_int"] = int(v_amount[:v_amount.index(".")])
                context["amount_feed"] = self.Count(int(v_amount[:v_amount.index(".")]))
        except models.Credit.DoesNotExist:
            return redirect(reverse('customer:create-credit'))
        return context
    
class NotaryCustomer(UpdateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/notary-fycas.html"
    
    # def get(self, request, *args, **kwargs):
    #     name = "Contrato " + str(datetime.today().date())
    #     print(name)
    #     return self.CreatePdf( template=self.template_name, name=name)

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
            credit = models.Credit.objects.get(customer=customer, id=self.kwargs.get('notary_id')) 
            context["amount"] = self.Amount(credit.amount)
            context["day_pay"] = self.DayNow(credit.day_pay)
            context["credit"] = credit
            if credit.amount_feed:
                print(credit.amount_feed)
                v_amount = str(credit.amount_feed)
                # print(v_amount[:v_amount.index(".")])
                context["amount_feed_int"] = int(v_amount[:v_amount.index(".")])
                context["amount_feed"] = self.Count(int(v_amount[:v_amount.index(".")]))
        except models.Credit.DoesNotExist:
            return redirect(reverse('customer:create-credit'))
        return context
    

    
    
    
class CreateCredit(CreateView, Options):
    model = models.Credit
    form_class = forms.CreditForm
    template_name = "customer/create-credit.html"

    def get(self, request, *args, **kwargs):
        customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
        try:
            credit = self.model.objects.get(customer=customer, is_active=True)
            return self.UpdateCredit(credit.id)
        except self.model.DoesNotExist:
            return super().get(request, *args, **kwargs)

            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
        context['c'] = customer
        return context
    
    def post(self, request, *args, **kwargs):
        c = models.Customer.objects.get(id=self.kwargs.get('pk'))
        f = self.form_class(request.POST)
        if f.is_valid():
            credit = f.save()
            credit.customer = c
            credit.save()
            URL = reverse('customer:detail-customer',  kwargs={'pk': c.id})
            return redirect(URL)
    
    
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

class ListCredit(ListView, Options):
        model = models.Credit
        template_name = "customer/list-credit.html"
        
        def get(self, request, *args, **kwargs):
            customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
            credit = self.model.objects.filter(customer__id = self.kwargs.get('pk'),is_active=True).exists()
            if credit:
                return super().get(request, *args, **kwargs)
            else:
                return self.CreateCredit(customer.id)
    
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['c'] = models.Customer.objects.get(id=self.kwargs.get('pk'))
            context['credit'] = self.model.objects.filter(customer__id=self.kwargs.get('pk'))

            return context
        
        

# Data Credito del Cliente 
class DataCredit(UpdateView):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/data-credit-customer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        return context
    
    
    
    