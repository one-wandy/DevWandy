from django.shortcuts import render
from django.views.generic import *
from . import forms
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from .mixing import *
from .mixing import Options
import os
from datetime import datetime, timedelta
from twilio.rest import Client  
import time
import locale
from datetime import datetime
import sys
from num2words import num2words
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.utils import timezone


class Dashboard(TemplateView, Options):
    template_name = "base/dashboard.html"
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
               return redirect(reverse('customer:search-company'))
        return super().get(request, *args, **kwargs)    
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        creditos = models.Credit.objects.filter(company=self.Company(), is_active = True)
        total_inversion = 0
        for credito in creditos:
            total_inversion += credito.amount

        context['total_inversion'] = total_inversion
        context['company'] = self.Company()
        context['customer_count'] = models.Customer.objects.filter(is_active = True, company = self.Company()).count()
        context['credit_count'] = models.Credit.objects.filter(is_active = True, company = self.Company()).count()
        context['s'] = intcomma(3232)

        return context
    
    
    # Esta vista agrega los clientes de manera externa a la empresa
class AddCustomer(CreateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/create-customer.html"
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = models.Company.objects.get(id=self.kwargs.get('pk'))
        return context
    
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('cedula-fast') != None:
                username = request.POST.get("cedula-fast")
                password = request.POST.get("numero-fast")
                try:
                    user = authenticate(username=username, password=password,)
                    print(user)
                    if user is not None:
                        login(request, user)
                        return redirect(reverse('customer:dashboard'))
                    else:
                        autenticado = False
                        mensaje = f"({username} o {password }) " 
                except User.DoesNotExist:
                    autenticado = False
                return redirect(reverse('customer:search-company'))
        
        else:
            f = self.form_class(request.POST, request.FILES)
            if f.is_valid():
                f.instance.img2 = request.FILES.get('img1')
                f.instance.company = models.Company.objects.get(id=self.kwargs.get('pk'))
                f.instance.nacimiento = request.POST.get('date-customer')
                f.instance.monto_requerido = request.POST.get('form-select-monto')
                f.instance.fines = request.POST.get('form-select')
                print(request.POST.get('form-select-sexo'))
                f.instance.sexo =  request.POST.get('form-select-sexo')
                f.instance.name = f.instance.name.title()
                f.instance.last_name = f.instance.last_name.title()
                f.instance.municipio = request.POST.get('form-select-muni')
                f.save()

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
        self.convertir_todos_los_campos_credit_a_mayusculas()
        if not request.user.is_authenticated:
               return redirect(reverse('customer:search-company'))
        return super().get(request, *args, **kwargs)
   
    def convertir_todos_los_campos_credit_a_mayusculas(self):
        creditos = self.model.objects.all()
        for credito in creditos:
            for field in credito._meta.fields:
                if isinstance(getattr(credito, field.name), str):  # Verifica si el campo es una cadena
                    setattr(credito, field.name, getattr(credito, field.name).title())
            credito.save()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fecha_actual = datetime.now()
        count_customer = self.request.POST.get('20-customer')
        customer = self.request.POST.get('send-data')

        if self.request.method == 'POST':
            if  self.request.POST.get('noti') != None:
                context['company'] = self.Company()
                context['customer'] = self.model.objects.filter(is_active = True, company = self.Company(),
                                    customer_verify = False).order_by('-id')
            if customer != None:                
                context['customer'] = self.model.objects.filter(id=int(customer))
                context['company'] = self.Company()
                ls = self.model.objects.filter(id=int(customer),company = self.Company(),)
                context['true'] = True
                return context

            if count_customer != None:
                    filter_client = self.model.objects.filter(is_active = True, company = self.Company(),
                                        customer_verify = True, 
                                    ).order_by('-id')[:int(count_customer)]
                    context['customer'] = filter_client
                    context['company'] = self.Company()
                    context['count_client'] = int(filter_client.count())
        else:
            filter_client = self.model.objects.filter(is_active = True, company = self.Company(),
                                    customer_verify = True ).order_by('-id')[:15]
            context['customer'] = filter_client
            context['company'] = self.Company()
            context['count_client'] = int(filter_client.count())
        
        context['customer_ramdon'] = self.model.objects.filter(is_active = True, company = self.Company(),).order_by('?')[:6]
        context['company'] = self.Company()
        context['fecha_actual'] =  fecha_actual.strftime("%d / %B / %Y").capitalize()
        context['customer_count'] = self.model.objects.filter(is_active = True, company = self.Company(),
                                    customer_verify = True).count()
        context['new_customer'] = self.model.objects.filter(is_active = True, company = self.Company(),
                                    customer_verify = False).count()
        context['day_pay'] = self.Day15_or_30()
        context['day_pay_2'] = self.Day_Pay()
        context['count_customer'] = count_customer
        return context
    
    def Day_Pay(self):
        today = datetime.today()
        day = today.day

        if day == 15:
            return True
        elif day == 30:
            return True
        else: 
            return False
    def Day15_or_30(self):
        today = datetime.today()
        day = today.day

        if day == 15:
            return f'Hoy es: {day} primer dia de cobro'
        elif day == 30:
            return f'Hoy es: {day} segundo dia de cobro'
        else:
            # Calcular días hasta el próximo 15 o 30
            if day < 15:
                next_cobro = 15
            elif day < 30:
                next_cobro = 30
            else:
                next_cobro = 15
                today += timedelta(days=30-today.day)

            days_until_next_cobro = (next_cobro - day) if day < next_cobro else (30 - day + 15)
            return f' Próximo dia de cobro en: {days_until_next_cobro} días'

    
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

            
        


class DetailCustomer(DetailView, Options):
    model = models.Customer
    form_class = forms.CustomerForm 
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
                context["amount_feed_int"] =  v_amount #int(v_amount[:v_amount.index(".")])  
                context["amount_feed"] = self.Count(v_amount) #self.Count(int(v_amount[:v_amount.index(".")]))
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
                context["amount_feed_int"] =  v_amount #int(v_amount[:v_amount.index(".")])  
                context["amount_feed"] = self.Count(v_amount) 
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
            c.monto_requerido = 'RD$' + '{:,}'.format(f.instance.amount)
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
        context['credit'] = self.model.objects.get(id=self.kwargs.get('pk'))
        context['company'] = self.Company()
        return context
    
    def form_valid(self, form_class):
            c = self.model.objects.get(id=self.kwargs.get('pk')).customer 
            c.monto_requerido = 'RD$' + '{:,}'.format(form_class.instance.amount)
            form_class.instance.customer = self.model.objects.get(id=self.kwargs.get('pk')).customer 
            form_class.instance.mont = Options.MontNow()
            form_class.instance.day = Options.DayNow(self,datetime.now().day)
            form_class.instance.day_number =  datetime.now().day
            form_class.instance.year = Options.YearNow(self, datetime.now().year)
            form_class.instance.year_number = datetime.now().year
            if form_class.instance.price_feed:
                self.model.objects.get(id=self.kwargs.get('pk')).credito.all().delete()

            if form_class.instance.amount:
                self.model.objects.get(id=self.kwargs.get('pk')).credito.all().delete()
                # Add your desired action here
            form_class.save()
            URL = reverse('customer:crear-credito',  kwargs={'pk': self.model.objects.get(id=self.kwargs.get('pk')).id})
            return redirect(URL)
    
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
        context['company'] = self.Company()
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
        context['company'] = self.Company()
        context['img'] = self.ImgApp(5)
        return context
    
    
    
class Approved(TemplateView, Options):
    template_name = "customer/approved.html"
    
    def get_context_data(self, **kwargs):
        credit = models.Credit.objects.filter(customer__id=self.kwargs.get('pk')).order_by('-id').last()
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()
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
        context['company'] = self.Company()
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
            return True
        
        
class ListCustomerSelect(ListView,Options):
    model = models.Customer
    template_name = "customer/list-customer-select.html"
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c'] = self.model.objects.all()
        return context
    

class CustomerProfile(TemplateView, Options):
    template_name = "customer-profile/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cb'] = models.CustomerDebit.objects.all()
        return context
    

class Mensensajeria(TemplateView, Options):
    template_name = "customer/mensajeria.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()
        context['cb'] = models.CustomerDebit.objects.all()
        return context
    

class Prestamos(ListView, Options):
    model = models.Customer
    template_name = "customer/prestamos.html"
    
   
    
        
#Esta vista agrega  a los clientes de manera internar a la empresa 
class Agregar(CreateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "components/agregar.html"
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()
        return context
    
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('cedula-fast') != None:
                username = request.POST.get("cedula-fast")
                password = request.POST.get("numero-fast")
                try:
                    user = authenticate(username=username, password=password,)
                    print(user)
                    if user is not None:
                        login(request, user)
                        return redirect(reverse('customer:agregar'))
                    else:
                        autenticado = False
                        mensaje = f"({username} o {password }) " 
                except User.DoesNotExist:
                    autenticado = False
                return redirect(reverse('customer:add-customer'))
        
        else:
            f = self.form_class(request.POST, request.FILES)
            if f.is_valid():
                f.instance.img2 = request.FILES.get('img1')
                f.instance.company = models.Company.objects.get(id=self.kwargs.get('pk'))
                f.instance.nacimiento = request.POST.get('date-customer')
                f.instance.monto_requerido = request.POST.get('form-select-monto')
                f.instance.fines = request.POST.get('form-select')
                print(request.POST.get('form-select-sexo'))
                f.instance.sexo =  request.POST.get('form-select-sexo')
                f.instance.name = f.instance.name.title()
                f.instance.last_name = f.instance.last_name.title()
                f.instance.municipio = request.POST.get('form-select-muni')
                f.save()
                # Creando Carpeta para el Cliente
                self.FileCreate(f.instance.name, f.instance.last_name)
                return redirect(reverse('maps:maps-customer'))
            else:
                return redirect(reverse('customer:add-customer'))
   
    
    
class Calendario(TemplateView, Options):
    template_name = "components/calendario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()

        return context
    
class Ubicaciones(TemplateView, Options):
    model = models.Customer
    template_name = "customer/ubicaciones.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()
        context['customer'] = self.model.objects.filter(is_active = True, 
                                        customer_verify = True)
        
        capital = 10000
        tasa_mensual = 15 / 100  # Convertir a decimal
        plazo = 4

        resultados = self.Calculadora_Francesa( capital, tasa_mensual, plazo)

        # Imprimir resultados
        for resultado in resultados:
            print(resultado)
            
        return context
    
    
    def Calculadora_Francesa(self, capital, tasa, plazo):
        # Calcular la cuota mensual
        cuotas = capital * tasa / (1 - (1 + tasa) ** -plazo)
        amortizacion = []
        saldo = capital
        total_intereses = 0

        for mes in range(1, plazo + 1):
            interes = saldo * tasa
            amortizacion_capital = cuotas - interes
            saldo -= amortizacion_capital
            total_intereses += interes

            amortizacion.append({
                "Mes": mes,
                "Cuota": round(cuotas, 2),
                "Interes": round(interes, 2),
                "AmortizacionCapital": round(amortizacion_capital, 2),
                "Saldo": round(saldo, 2)
            })
        
        return amortizacion

# Ejemplo de uso

class Configuraciones(TemplateView, Options):
    template_name = "components/configuraciones.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()
        context['configurations'] = models.ConfigurationCompany.objects.filter(is_active=True, company=self.Company())
        return context

from dateutil.relativedelta import relativedelta
from calendar import monthrange



class CrearCredito(TemplateView, Options):
    model = models.Cuota  # Define el modelo que se va a crear
    template_name = "customer/crear-credito.html"  # Nombre de la plantilla

    def post(self, request, *args, **kwargs):   
        self.RunCreditValidate()
        credit = models.Credit.objects.get(id=self.kwargs.get('pk'))
        capital = int(credit.amount)
        tasa = int(credit.tasa)
        plazo = int(credit.price_feed)
        
        print(self.Calculadora_Francesa(capital, tasa, plazo, credit))
    
        return super().get(request, *args, **kwargs)
    
    
    def Calculadora_Francesa(self, capital, tasa, plazo, credit):
        self.RunCreditValidate()
        if tasa != 0:
            pass
        else:
            tasa = 15
        tasa = tasa / 100
        if credit.credito.exists() == True:
            return 'Ya Existen cuotas para este credito'
        else:
            # Calcular la cuota mensual
            cuotas = capital * tasa / (1 - (1 + tasa) ** -plazo)
            saldo = capital
            total_intereses = 1

            def adjust_day_for_month(date, day):
                """Ajusta el día para que sea válido en el mes dado."""
                last_day_of_month = monthrange(date.year, date.month)[1]
                return min(day, last_day_of_month)

            day_pay = credit.day_pay
            

            start_date = credit.date

            for mes in range(1, plazo + 1):
                interes = saldo * tasa
                amortizacion_capital = cuotas - interes
                saldo -= amortizacion_capital
                total_intereses += interes

                # Ajusta el día al valor de day_pay para start_date
                last_day_of_month = monthrange(start_date.year, start_date.month)[1]
                if day_pay > last_day_of_month:
                    start_date = start_date.replace(day=last_day_of_month)
                else:
                    start_date = start_date.replace(day=day_pay)
                
                # Ajusta el end_date al valor de day_pay más 5
                end_date = start_date + timedelta(days=5)

                cuota = models.Cuota.objects.create(
                    credito=credit,
                    cuota=round(cuotas, 2) + 1,
                    start_date=start_date,
                    end_date=end_date,
                )

                # Incrementar el mes para la próxima iteración
                start_date = start_date + relativedelta(months=1)

            return 'Creado'

    def FiltrarCreditosAtrasados(self):
        today = datetime.now().date()
        
        creditos_atrasados = models.Credit.objects.filter(credito_atrasado=True)

        cuotas_vencidas = []

        # Convertir la tasa mensual de porcentaje a decimal
     

        for credito in creditos_atrasados:
            cuotas = models.Cuota.objects.filter(credito=credito, end_date__lt=today)

            for cuota in cuotas:
                tasa_decimal = cuota.credito.tasa / 100

                dias_mes = monthrange(cuota.end_date.year, cuota.end_date.month)[1]

                dias_atraso = (today - cuota.end_date).days

                cuota_fija = int(cuota.credito.amount_feed) + 1
                # Calcular la mora
                mora = ( cuota_fija * tasa_decimal) / dias_mes * dias_atraso

                cuota.dias_en_atraso = dias_atraso
                # Total con mora
                cuota.mora = mora
                cuota.cuota = cuota_fija + mora
                cuota.save()
                total_con_mora = int(cuota.cuota + mora)
                print(total_con_mora, 'Moras', dias_atraso)


            cuotas_vencidas.extend(cuotas)
        
        return creditos_atrasados, cuotas_vencidas


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.FiltrarCreditosAtrasados(), 'Siuu')
        self.RunCreditValidate()
        try:
                    models.Credit.objects.get(id=self.kwargs.get('pk'))
                    credit =  models.Credit.objects.get(id=self.kwargs.get('pk'))

                    all_credits = models.Credit.objects.filter(customer__id=credit.customer.id).order_by('-id')

                    customer_exist_credit = models.Customer.objects.get(id=credit.customer.id)
                    exist_credit = models.Credit.objects.filter(customer__id=credit.customer.id, estado_credito=False).exists()

                    # Añadir contexto adicional a la plantilla si es necesario
                    cuotas =  credit.credito.all()
                    p_x_c = 1
                    c_p = 0
                    
                    p_cuotas = 0
                    c_cuotas = cuotas.count()
                    for cu in cuotas:
                        p_x_c += cu.cuota
                        if cu.abonado > 0:
                            c_p += cu.abonado
                            
                        if cu.estado == True:
                            p_cuotas += 1

                    fecha_actual = datetime.now()
                    context['cal'] = self.CalFran(int(credit.amount), int(credit.tasa), int(credit.price_feed), 't') 
                    context['credit'] =  credit
                    context['cc'] = p_x_c - c_p
                    context['cp'] = c_p
                    context['all_credits'] = all_credits
                    context['c_cuotas'] = c_cuotas
                    context['exist_credit'] = exist_credit 
                    context['p_cuotas'] = p_cuotas
                    context['today'] = timezone.now().date()
                    context['c'] =  credit.customer
                    context['fecha_actual'] =  fecha_actual.strftime("%d/%m/%Y").capitalize()

                    if credit.credito.exists() == True:
                            context['cuotas'] = cuotas
        except models.Credit.DoesNotExist:
            context['error'] = "No se encontró el crédito especificado."
            
        context['company'] = self.Company()
        return context
    
    
    
    def CalFran(self, capital, tasa, plazo, filter_l):

            if tasa != 0:
                tasa = tasa / 100
            else:
                tasa = 0.15
            # Calcular la cuota mensual
            cuotas = capital * tasa / (1 - (1 + tasa) ** -plazo)
            saldo = capital
            total_intereses = 1

            for mes in range(1, plazo + 1):
                interes = saldo * tasa
                amortizacion_capital = cuotas - interes
                saldo -= amortizacion_capital
                total_intereses += interes
                print(total_intereses)
            if filter_l == 's':
                return saldo
            elif filter_l == 't':
                return  int(total_intereses)
            else:
                return cuotas




class ListadoCredit_rederict(View):
        model = models.Credit
        def get(self, request, *args, **kwargs):
            customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
            credit = self.model.objects.filter(customer__id=customer.id).last()
            if credit:  # Replace with your actual condition
                URL = reverse('customer:crear-credito',  kwargs={'pk': credit.id})
                return redirect(URL)
            else:
                URL = reverse('customer:create-credit-new',  kwargs={'pk': customer.id})
                return redirect(URL)





class CreateCreditNew(CreateView, Options):
        model = models.Credit
        form_class = forms.CreditForm
        template_name = "customer/crear-creadito-new.html"

        # def get(self, request, *args, **kwargs):
        #     customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
        #     try:
        #         credit = self.model.objects.get(customer=customer, is_active=True)
        #         return self.UpdateCredit(credit.id)
        #     except self.model.DoesNotExist:
        #         return super().get(request, *args, **kwargs)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
            context['c'] = customer
            context['company'] = self.Company()
            return context

        def form_valid(self, form_class):
            customer = models.Customer.objects.get(id=self.kwargs.get('pk'))
            form_class.instance.customer = customer
            form_class.instance.mont = Options.MontNow()
            form_class.instance.day = Options.DayNow(self,datetime.now().day)
            form_class.instance.day_number =  datetime.now().day
            form_class.instance.year = Options.YearNow(self, datetime.now().year)
            form_class.instance.year_number = datetime.now().year
            form_class.save()
            URL = reverse('customer:crear-credito',  kwargs={'pk': form_class.instance.id})
            return redirect(URL)



class ListAllCredits(ListView, Options):
    model = models.Credit
    template_name = "customer/list-all-credits.html"
    
    def get(self, request, *args, **kwargs):
        self.RunCreditValidate()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pendiente_credit = self.model.objects.filter(estado_credito=False, credito_atrasado=True).count()
        saldado_credit = self.model.objects.filter(estado_credito=True).count()
        credits_count = self.model.objects.all().count()
        context['credits_count'] = credits_count
        context['all_credits'] = self.model.objects.filter(estado_credito=False).order_by('-id')
        context['pendiente_credit'] = pendiente_credit
        context['saldado_credit'] = saldado_credit
        context['company'] = self.Company()
        if self.request.method == 'POST':
            print('siuu')
            
            if  self.request.POST.get('pendientes') != None:
                context['all_credits'] = self.model.objects.filter(estado_credito=False, credito_atrasado=True).order_by('-id')
            if  self.request.POST.get('saldado') != None:
                context['all_credits'] = self.model.objects.filter(estado_credito=True).order_by('-id')
        else:
            context['all_credits'] = self.model.objects.filter(estado_credito=False).order_by('-id')
        return context



class Empresa(TemplateView, Options):
        template_name = "empresa/empresa.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['company'] = self.Company()
            # context['employees'] = models.Employee.objects.filter(company=self.Company())
            return context


class Calculadora(TemplateView, Options):
        template_name = "components/clc-extensa.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['company'] = self.Company()
            # context['employees'] = models.Employee.objects.filter(company=self.Company())
            return context


class SearchCompany(TemplateView, Options):
        template_name = "components/search-company.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['all_company'] = models.Company.objects.all()
            # context['employees'] = models.Employee.objects.filter(company=self.Company())
            return context



class SelecForm(CreateView, Options):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "components/select-form.html"
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()
        return context
    
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('cedula-fast') != None:
                username = request.POST.get("cedula-fast")
                password = request.POST.get("numero-fast")
                try:
                    user = authenticate(username=username, password=password,)
                    print(user)
                    if user is not None:
                        login(request, user)
                        return redirect(reverse('customer:agregar'))
                    else:
                        autenticado = False
                        mensaje = f"({username} o {password }) " 
                except User.DoesNotExist:
                    autenticado = False
                return redirect(reverse('customer:add-customer'))
        
        else:
            f = self.form_class(request.POST, request.FILES)
            if f.is_valid():
                f.instance.company = models.Company.objects.get(id=self.kwargs.get('pk'))
                f.instance.nacimiento = request.POST.get('date-customer')
                f.instance.monto_requerido = request.POST.get('form-select-monto')
                f.instance.fines = request.POST.get('form-select')
                print(request.POST.get('form-select-sexo'))
                f.instance.sexo =  request.POST.get('form-select-sexo')
                f.instance.name = f.instance.name.title()
                f.instance.last_name = f.instance.last_name.title()
                f.instance.municipio = request.POST.get('form-select-muni')
                f.save()
                # Creando Carpeta para el Cliente
                self.FileCreate(f.instance.name, f.instance.last_name)
                return redirect(reverse('maps:maps-customer'))
            else:
                return redirect(reverse('customer:add-customer'))