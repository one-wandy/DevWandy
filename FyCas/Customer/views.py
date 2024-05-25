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
from twilio.rest import Client  
import time


class Dashboard(TemplateView, Options):
    template_name = "base/dashboard.html"
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
               return redirect(reverse('customer:add-customer'))
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = self.Setting()
        return context
    
    
class AddCustomer(CreateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/create-customer.html"
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = self.Setting()
        context['img1'] = self.ImgApp(2)
        context['img2'] = self.ImgApp(3)
        context['img3'] = self.ImgApp(4)
        return context
    
    
    def post(self, request, *args, **kwargs):
        f = self.form_class(request.POST, request.FILES)
        if f.is_valid():
            f.instance.nacimiento = request.POST.get('date-customer')
            f.instance.monto_requerido = request.POST.get('form-select-monto')
            f.instance.fines = request.POST.get('form-select')
            print(request.POST.get('form-select-sexo'))
            f.instance.sexo =  request.POST.get('form-select-sexo')
            f.instance.name = f.instance.name.title()
            f.instance.last_name = f.instance.last_name.title()
            f.save()
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
    
class ListCustomer(ListView,Options):
    model = models.Customer
    template_name = "customer/list-customer.html"
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
               return redirect(reverse('customer:add-customer'))
        return super().get(request, *args, **kwargs)
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count_customer = self.request.POST.get('20-customer')
        customer = self.request.POST.get('send-data')
        if self.request.method == 'POST':
            if customer != None:
                print(customer)
                
                context['customer'] = self.model.objects.filter(id=int(customer))
                ls = self.model.objects.filter(id=int(customer))
                print(ls)
                context['true'] = True
                return context

            if count_customer != None:
                    context['customer'] = self.model.objects.filter(is_active = True, 
                                                    ).order_by('-id')[:int(count_customer)]
                # else:
        else:
            
            context['customer'] = self.model.objects.filter(is_active = True, 
                                                    customer_verify = True ).order_by('-id')[:4]
                
        context['setting'] = self.Setting()
        context['customer_count'] = self.model.objects.filter(is_active = True).count()

        return context
    
    
    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
class UpdateCustomer(UpdateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/update-customer.html"
    
    def get(self, request, *args, **kwargs):
            customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
            # credit = self.model.objects.filter(customer__id = self.kwargs.get('pk'),is_active=True).exists()
            # if credit:
            return super().get(request, *args, **kwargs)
            # else:
                # return self.CreateCredit(customer.id)
    
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
    template_name = "customer/user-profile.html"
    
    def get(self, request, *args, **kwargs):
        print(request.user)
        if not request.user.is_authenticated:
               return redirect(reverse('customer:add-customer'))
        return super().get(request, *args, **kwargs)
    
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
        # customer.delete()
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
        customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
        c = models.Credit.objects.get(customer=customer, id=self.kwargs.get('credit_id')) 
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['mont'] = c.mont
        context['day'] = c.day
        context['day_number'] = c.day_number
        context['year'] = c.year
        context['year_number'] = c.year_number
        context["amount"] = c.amount
        # context["day_pay"] = c.day_pay
        context["credit"] = c
        try:
            context["amount"] = self.Amount(c.amount)
            context["day_pay"] = self.DayNow(c.day_pay)
            context["credit"] = c
            if c.amount_feed:
                v_amount = str(c.amount_feed)
                # print(v_amount[:v_amount.index(".")])
                context["amount_feed_int"] = int(v_amount[:v_amount.index(".")])
                context["amount_feed"] = self.Count(int(v_amount[:v_amount.index(".")]))
        except models.Credit.DoesNotExist:
            return redirect(reverse('customer:create-credit'))
        return context
    
class NotaryCustomer(UpdateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/fycas-notary.html"
    
    # def get(self, request, *args, **kwargs):
    #     name = "Contrato " + str(datetime.today().date())
    #     print(name)
    #     return self.CreatePdf( template=self.template_name, name=name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk'))
        try:
            c = models.Credit.objects.get(customer=customer, id=self.kwargs.get('notary_id')) 
            context['mont'] = c.mont
            context['day'] = c.day
            context['day_number'] = c.day_number
            context['year'] = c.year
            context['year_number'] = c.year_number
            context["amount"] = self.Amount(c.amount)
            context["day_pay"] = self.DayNow(c.day_pay)
            context["credit"] = c
            if c.amount_feed:
                v_amount = str(c.amount_feed)
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
        v_amount = str(f.instance.amount_feed)
        if f.is_valid():
            f.instance.customer = c
            f.instance.mont = self.MontNow(datetime.now().month)
            f.instance.day = self.DayNow(datetime.now().day)
            f.instance.day_number =  datetime.now().day
            f.instance.year = self.YearNow(datetime.now().year)
            f.instance.year_number = datetime.now().year
            f.save()
            URL = reverse('customer:detail-customer',  kwargs={'pk': c.id})
            return redirect(URL)
    
    
class UpdateCredit(UpdateView, Options):
    model = models.Credit
    form_class = forms.CreditForm
    template_name = "customer/update-credit.html"
    
    def get(self, request, *args, **kwargs):
            credit = self.model.objects.filter(id = self.kwargs.get('pk'),is_active=True).exists()
            if credit:
                return super().get(request, *args, **kwargs)
            else:
                return self.CreateCredit(credit.customer.id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.get(id=self.kwargs.get('pk')).customer 
        return context
    
    def form_valid(self, form_class):
            form_class.instance.customer = self.model.objects.get(id=self.kwargs.get('pk')).customer 
            form_class.instance.mont = self.MontNow(datetime.now().month)
            form_class.instance.day = self.DayNow(datetime.now().day)
            form_class.instance.day_number =  datetime.now().day
            form_class.instance.year = self.YearNow(datetime.now().year)
            form_class.instance.year_number = datetime.now().year
            form_class.save()
            return self.List_Redirect()
    
    # def post(self, request, *args, **kwargs):   
    #     f = self.form_class(request.POST)
    #     if f.is_valid():     
    #     

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
    
    # Detalle del prestamo para enviar a quien va aprobar el prestamo
class DetailCreditCustomer(DetailView, Options):
    model = models.Credit
    form_class = forms.PayCreditForm
    template_name = "customer/detail-credit-customer.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['credit'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['setting'] = self.Setting()
        context['form'] = forms.PayCreditForm

        return context

    def post(self, request, *args, **kwargs):   
        f = self.form_class(request.POST, request.FILES)
        if f.is_valid():
            f.instance.credit = self.model.objects.get(id=self.kwargs.get('pk'))
            f.save()     
            return self.List_Redirect()
        else:
            return super().get(request, *args, **kwargs)

    
class NoApproved(TemplateView, Options):
    template_name = "customer/not-approved.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = self.Setting()
        context['img'] = self.ImgApp(5)
        return context
    
    
    
class Approved(TemplateView, Options):
    template_name = "customer/approved.html"
    
    def get_context_data(self, **kwargs):
        credit = models.Credit.objects.filter(customer__id=self.kwargs.get('pk')).order_by('-id').last()
        context = super().get_context_data(**kwargs)
        context['setting'] = self.Setting()
        context['c'] = models.Customer.objects.get(id=self.kwargs.get('pk'))
        context['credit'] = credit
        context['img'] = self.ImgApp(1)

        return context
    
    
    
class CreateCustomerDebit(CreateView, Options):
    model = models.CustomerDebit
    form_class = forms.CustomerDebit
    template_name = "customer/create-customer-debeit.html"
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = self.Setting()
        # context['form'] = forms.CustomerDebit
        return context
    

    def post(self, request, *args, **kwargs):
        f = self.form_class(request.POST)
        if f.is_valid():
            f.save()
        else:
            print(f)
        URL = reverse('customer:create-customer-debit')
        return redirect(URL)
    
    
class MensajeCustomerDebit(TemplateView, Options):
    template_name = "customer/mensaje-customer-debit.html"
    
    
    def post(self, request, *args, **kwargs):
        customer_debit = models.CustomerDebit.objects.all()
        for cb in customer_debit:
            print(f'Recordatorio enviado a: {cb.name}, {cb.number}')
            self.Send_WhatsApp_Message(cb.name, cb.number)
            time.sleep(20) 
        return super().get(request, *args, **kwargs)
      
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cb'] = models.CustomerDebit.objects.all()
        return context
    
    
    def Send_WhatsApp_Message(self, name, number):
            account_sid = 'AC32b5e94ce632aabd0a278a56e16bd44a'
            auth_token = 'a61c8b622e93ada5958d69dacef7c461'
            client = Client(account_sid, auth_token)

            Msm = f"Recordatorio de Pago - Grupo FyCas \n \nEstimado {name}: \n\nPor medio del presente mensaje, le recordamos que tiene un saldo de pago pendiente. Su puntualidad en los pagos es muy importante para nosotros, por lo que le solicitamos amablemente que realice su pago lo antes posible. \n \nSi ya ha realizado su pago, por favor ignore este mensaje."
            message = client.messages.create(
                  body= Msm,
                  from_= '+13344384583',
                  to= f'+1{number}' )
            
            # msg = client.messages.create(
            #       from_='whatsapp:+18295577196',
            #       body='Mensaje enviado por Wandy Olivares',
            #       to='whatsapp:+18295577196')
            return True
        
        
class ListCustomerSelect(ListView,Options):
    model = models.Customer
    template_name = "customer/list-customer-select.html"
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.all()
        return context
    