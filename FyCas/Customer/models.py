from django.db import models
from django.utils import timezone
from PIL import Image
import os
from django.core.files.base import ContentFile
from io import BytesIO

from django.contrib.auth.models import User




# Create your models here.

class Customer(models.Model):
    company= models.ForeignKey('Company', on_delete=models.CASCADE,  blank=True, null=True, related_name="company_customer")
    # Para el tema de las solicitudes, cuando el user ingresa por primera vez el estado permanece false durante los proximos 7 dias, sera descartado y eliminado de la base de datos ya que su aprobacion no fue verificada por lo tanto no cambio a " True " pero se guardada su DNI en una base de datos adicional mas adelante p
    not_aprobado = models.BooleanField(default=False,  blank=True)
    # Si 
    customer_verify = models.BooleanField(default=False,  blank=True)
   
    debit = models.BooleanField(default=False,  blank=True)
    
    debit_visit = models.BooleanField(default=False,  blank=True)
    debit_follow = models.BooleanField(default=False,  blank=True)

    
    # Datos Opcionales
    vehiculo = models.BooleanField(default=False,  blank=True)
    casa = models.BooleanField(default=False,  blank=True)
    tierra = models.BooleanField(default=False,  blank=True)
    
    hijos = models.BooleanField(default=False,  blank=True)
    saldar_deudas = models.BooleanField(default=False,  blank=True)

    
    # Preguntas 
    familiar_en_fycas = models.BooleanField(default=False, blank=True)
    fue_recomendado = models.BooleanField(default=False,  blank=True)
    
    monto_requerido = models.CharField(max_length=255, default='',  blank=True)
    fines = models.CharField(max_length=255, default='',  blank=True)
    

    is_active = models.BooleanField(default=True)
    name = models.CharField( max_length=255, )#Nombre
    last_name = models.CharField( max_length=255)#Apellido
    number = models.CharField( max_length=20, )#Numero local o Movile
    address = models.CharField( max_length=255, blank=True)#Direccion de donde recide
    email = models.EmailField(null=True, blank=True)#Correo electronico
    amount_purpose = models.TextField(blank=True, max_length=355)#Proposito por el que se solicita el prestamo
    work_information = models.TextField(blank=True, max_length=300)#Informacion donde trabaja
    references_peopple = models.TextField(blank=True, max_length=500)#Personas referentes
    dni = models.CharField( max_length=100) #Numero de Identidad
    amount = models.IntegerField(null=True)#Monto 
    no_account = models.IntegerField(default=0) #Numero de Cuentaloooo
    
    img1 = models.ImageField(upload_to="media/",  blank=True, null=True, default=None)
      #Foto de Cedula delantera
    img2 = models.ImageField(upload_to="media/", blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        # Save the original instance first to ensure img1 is available
        super(Customer, self).save(*args, **kwargs)

        if self.img1:
            try:
                img2 = self.img1.path
                # Open the original image
                img1_path = self.img1.path
                img1 = Image.open(img1_path)

                # Resize img1 to 250p resolution
                img1.thumbnail((50, 50))
                img1_io = BytesIO()
                img1.save(img1_io, format=img1.format, quality=50)  # Reduce quality to reduce file size

                self.img1.save(os.path.basename(self.img1.name), ContentFile(img1_io.getvalue()), save=False)
            except FileNotFoundError:
                pass

        super(Customer, self).save(*args, **kwargs)


    #Foto de Cedula tracera
    name_r1 = models.CharField( max_length=255,  )#Nombre
    name_r2 = models.CharField( max_length=255,  )#Nombre
    number_r1 = models.CharField(default="",  max_length=30)#Numero local o Movile
    number_r2 = models.CharField(default="",  max_length=30  )#Numero local o Movile
    
    # CaptureLocation
    lat = models.CharField(blank=True, max_length=100000000050005, default='')
    lon = models.CharField(blank=True, max_length=100000000000000055, default='')
    
    # Tipo de Entrada
    type_input = models.CharField(blank=True, max_length=2, default='P')
    #Sexo
    sexo = models.CharField(blank=True, max_length=2, default='M')
    # Estado Civil 
    estado_civil = models.CharField(blank=True, max_length=2, default='')
    # Ocupacion 
    ocupacion = models.CharField(blank=True, max_length=25, default='Estudiante')
    # Codigo de cliente
    code_customer = models.CharField(blank=True, max_length=122000, default='')
    # Date 
    nacimiento = models.CharField(blank=True, max_length=40, default='10/11/2001')
    # Nacionalidad 
    nacionalidad = models.CharField(blank=True, max_length=25, default='DOMINICANA')
    # Direccion
    direccion = models.CharField(blank=True, max_length=255, default='')
    # Sector
    sector = models.CharField(blank=True, max_length=455, default='')
    # Calle/Numero
    calle_numero = models.CharField(blank=True, max_length=255, default='')
    # municipio
    municipio = models.CharField(blank=True, max_length=255, default='')
    # Cuidad 
    ciudad = models.CharField(blank=True, max_length=250, default='Santo Domingo')
    # provincia
    provincia = models.CharField(blank=True, max_length=255, default='SANTO DOMINGO DE GUZMAN')
    # Pais
    pais = models.CharField(blank=True, max_length=255, default='REPUBLICA DOMINICANA')
    # dir_referencia
    dir_referencia = models.CharField(blank=True, max_length=255, default='')
    # Numero de telefono de la empresa
    phone = models.CharField(blank=True, max_length=18, default='')
    
    # Datos donde labura
    # Empresa donde trabaja  
    empresa_trabaja = models.CharField(blank=True, max_length=255, default='')
    # Cargo
    cargo = models.CharField( max_length=255, default='')
    # Direccion 
    direccion_trabajo = models.CharField(blank=True, max_length=255, default='')
    # Sector 
    sector = models.CharField(blank=True, max_length=244, default='')
    # Calle
    calle_numero_trabajo = models.CharField(blank=True, max_length=255, default='')
    # Municipio 
    municipio_trabaja = models.CharField(blank=True, max_length=255, default='')
    # Ciudad 
    ciudad_trabaja = models.CharField(blank=True, max_length=255, default='')
    # provins
    provincia_trabajo = models.CharField(blank=True, max_length=255, default='SANTO DOMINGO DE GUZMAN')
    # pais
    pais_trabajo = models.CharField(blank=True, max_length=244, default='REPUBLICA DOMINICANA')
    # dir_referencia
    dir_referencia_trabajo = models.CharField(blank=True, max_length=244, default='')
    #Salario de M
    salario_m = models.CharField( max_length=233, default='')
    # Moneda 
    moneda = models.CharField(blank=True, max_length=3, default='RD$')  
    # Datos de la cuantas 
    # Realcion tipo uno
    relacion_tipo = models.CharField(blank=True, max_length=233, default='1')
    # Fecha de Apertura
    fecha_apertura = models.CharField(blank=True, max_length=233, default='')
    # Fecha de Vencimiento
    fecha_vencimiento = models.CharField(blank=True, max_length=233, default='')
    # Fecha del ultimo pago
    fecha_ultimo_pago = models.CharField(blank=True, max_length=233, default='')
    # Numero de cuenta 
    numeoro_cuenta = models.CharField(blank=True, max_length=233, default='')
    # Estatus 
    estatus = models.CharField(blank=True, max_length=233, default='')
    # Tipo de prestamo
    tipo_prestamo = models.CharField(blank=True, max_length=233, default='N')
    # Moneda 
    moneda_prestamo = models.CharField(blank=True, max_length=233, default='RD$')
    # Credito Aprovado 
    credito_aprovado = models.CharField(blank=True, max_length=233, default='')
    #Balance al Corte
    balance_corte = models.CharField(blank=True, max_length=233, default='')
    #Monto Adeudado
    monto_adeudado = models.CharField(blank=True, max_length=233, default='')
    # Pago mandatotio o cuota
    pago_mandatorio_cuota = models.CharField(blank=True, max_length=233, default='')
    # Monto Ultimo Pago
    monto_ultimo_pago = models.CharField(blank=True, max_length=233, default='') 
    # Total de Atraso
    total_atraso = models.CharField(blank=True, max_length=233, default='')
    # Tasa de interes
    tasa_interes = models.CharField(blank=True, max_length=233, default='0.15')
    # Forma de pago 
    forma_pago = models.CharField(blank=True, max_length=233, default='Mensual')
    # Cantidad de Cuota
    cantidad_cuota = models.CharField(blank=True, max_length=233, default='6')
    atraso1_30 = models.CharField(blank=True, max_length=233, default='')
    atraso31_60 = models.CharField(blank=True, max_length=233, default='')
    atraso61_90 = models.CharField(blank=True, max_length=233, default='')
    atraso91_120 = models.CharField(blank=True, max_length=233, default='')
    atraso121_150 = models.CharField(blank=True, max_length=233, default='')
    atraso151_180 = models.CharField(blank=True, max_length=233, default='')
    atraso181_o_mas = models.CharField(blank=True, max_length=233, default='')

    day_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name}, {self.last_name}, {self.company}'


class Credit(models.Model):
    company= models.ForeignKey('Company', on_delete=models.CASCADE,  blank=True, null=True, related_name="company_credit")
    customer = models.ForeignKey(Customer, null=True, blank=True, 
                    on_delete=models.CASCADE, related_name="credit")
    amount = models.IntegerField(default=10000) # Este es el capital que si varia, esto para el ajuste de los abonos al capital
    capital_no_variable = models.IntegerField(default=1, blank=True, null=True) # Este capital no varia
    name = models.CharField(max_length=100)
    #Numero de Cuenta
    price_feed = models.IntegerField(default=1)
    dni = models.TextField(default="")
    no_account = models.TextField() 
    #if mode_pay is True Appli 
    mode_pay = models.BooleanField(default=False)
    day_pay = models.IntegerField(default=30)
    is_active = models.BooleanField(default=True)
    #is active rederict at diferens view
    mont = models.CharField(max_length=100, default="")
    day = models.CharField(max_length=100, default="")
    day_number = models.CharField(max_length=100, default="")
    year = models.CharField(max_length=100, default="")
    year_number = models.CharField(max_length=100, default="")
    amount_str = models.CharField(max_length=100, default="")
    amount_feed_int = models.CharField(max_length=100, default="")
    amount_feed = models.CharField(max_length=100, default="")
    # Day Create
    day_created = models.DateField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    #Estado de  credito
    tasa = models.IntegerField(default=15)
    plazo = models.IntegerField(default=1)
    estado = models.BooleanField(default=False,  null=True, blank=True) 


    precio_a_saldar = models.IntegerField(default=1, blank=True)
    estado_credito = models.BooleanField(default=False,  null=True, blank=True)
    credito_atrasado = models.BooleanField(default=False,  null=True, blank=True)
    
    def __str__(self):
        return f'{self.customer.name} {self.customer.last_name}, {self.amount}, {self.date}'

class Cuota(models.Model):
        credito = models.ForeignKey(Credit, null=True, blank=True, 
                    on_delete=models.CASCADE, related_name="credito")
        cuota = models.IntegerField(default=0,  null=True, blank=True) #Precio de la cuota
        abonado = models.IntegerField(default=0,  null=True, blank=True) #Precio de la cuota
        restante = models.IntegerField(default=0,  null=True, blank=True) #Precio de la cuota
        
        capital = models.IntegerField(default=0,  null=True, blank=True) #Capital del credito
        capital_restante = models.IntegerField(default=0,  null=True, blank=True) #Capital que restaba 
        creado = models.DateField(default=timezone.now,  null=True, blank=True) #Dia en el que se creo la cuota mandatoria
        pago = models.CharField(default='', max_length=20,  null=True, blank=True) #Dia en que se realizo el pago
        estado = models.BooleanField(default=False,  null=True, blank=True) #Estado de  pago

        start_date = models.DateField(default=timezone.now, null=True, blank=True)
        end_date = models.DateField(null=True, blank=True)

        last_pay = models.DateField(default=timezone.now, null=True, blank=True)

        last_time_pay = models.TimeField(default=timezone.now)

        dias_en_atraso = models.IntegerField(default=0,  null=True, blank=True) #Precio de la cuota
        mora = models.IntegerField(default=0,  null=True, blank=True) #Precio de la cuota

        # def save(self, *args, **kwargs):
        #     if self.start_date:
        #         next_month = self.start_date.month % 12 + 1
        #         year_increment = (self.start_date.month + 1) // 13
        #         self.end_date = self.start_date.replace(month=next_month, year=self.start_date.year + year_increment)
        #     elif self.end_date:
        #         next_month = self.end_date.month % 12 + 1
        #         year_increment = (self.end_date.month + 1) // 13
        #         self.end_date = self.end_date.replace(month=next_month, year=self.end_date.year + year_increment)
        #     super(Cuota, self).save(*args, **kwargs)

        credito_atrasado = models.BooleanField(default=False,  null=True, blank=True)
        
        def __str__(self):
            return  f" {self.credito.customer.name} {self.credito.customer.last_name},    {str(self.cuota)}"
        
        
        
class PayCredit(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="media/", blank=True, null=True, default="") 
    


    
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True, related_name="company")
    name = models.CharField(blank=True, max_length=233, default='Grupo Fycas')
    description = models.TextField(blank=True, null=True, default='Grupo Fycas')
    Icon = models.ImageField(upload_to="media/", blank=True, null=True, 
    default="media/img-default/img.png")
    Icon_img = models.ImageField(upload_to="media/", blank=True, null=True, 
    default="media/img-default/img.png")
    phone = models.CharField(blank=True, max_length=233, default='829-557-7196')
    email = models.CharField(blank=True, null=True, max_length=233,)
    EMAIL_PROVIDERS = [
        ('@gmail.com', 'Gmail'),
        ('@icloud.com', 'iCloud'),
        ('@yahoo.com', 'Yahoo'),
        ('@outlook.com', 'Outlook'),
        ('@other', 'Other'),
    ]
    email_provider = models.CharField(max_length=50, choices=EMAIL_PROVIDERS, default='gmail', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    rnc = models.CharField(max_length=50, blank=True, null=True, default='')
    #Foto de Cedula tracera
    direccion = models.CharField( max_length=555, blank=True, null=True, default='')
    instagrem = models.CharField( max_length=255, blank=True, null=True, default='')
    facebook = models.CharField( max_length=255, blank=True, null=True, default='')
    twitter = models.CharField( max_length=255, blank=True, null=True, default='')
    whatsapp = models.CharField( max_length=255, blank=True, null=True, default='')

    # Configuracion de la UI para la compania
    bg_enfasis = models.CharField(blank=True, max_length=233, default='rgb(83, 137, 255)') #color de enfasis de la ui
    key = models.TextField(blank=True,) #color de enfasis de la ui

    contrato = models.TextField(blank=True,) #color de enfasis de la ui
    notarial = models.TextField(blank=True,) #color de enfasis de la ui

    
    def __str__(self):
        return self.name



class Img(models.Model):
    name = models.CharField(blank=True, max_length=233, default='Money')
    Icon = models.ImageField(upload_to="media/", blank=True, null=True) 
    
    def __str__(self):
        return self.name


class CustomerDebit(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    dni = models.CharField(max_length=20, null=True, blank=True, default=None)
    day_created = models.DateField(default=timezone.now, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class CashControl(models.Model):
        date = models.DateField(default=timezone.now)
        opening_balance = models.DecimalField(max_digits=10, decimal_places=2)
        closing_balance = models.DecimalField(max_digits=10, decimal_places=2)
        total_income = models.DecimalField(max_digits=10, decimal_places=2)
        total_expenses = models.DecimalField(max_digits=10, decimal_places=2)
        notes = models.TextField(blank=True, null=True)

        def __str__(self):
            return f"Cash Control for {self.date}"


# Comfiguracion 
class ConfigurationCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, 
    related_name="configuration_company", blank=True, null=True)
    name = models.CharField(max_length=100, default="Configuracion")
    img = models.ImageField(upload_to="media/", blank=True, null=True) 
    svg = models.TextField(default='<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-balloon-heart" viewBox="0 0 16 16"><path fill-rule="evenodd" d="m8 2.42-.717-.737c-1.13-1.161-3.243-.777-4.01.72-.35.685-.451 1.707.236 3.062C4.16 6.753 5.52 8.32 8 10.042c2.479-1.723 3.839-3.29 4.491-4.577.687-1.355.587-2.377.236-3.061-.767-1.498-2.88-1.882-4.01-.721zm-.49 8.5c-10.78-7.44-3-13.155.359-10.063q.068.062.132.129.065-.067.132-.129c3.36-3.092 11.137 2.624.357 10.063l.235.468a.25.25 0 1 1-.448.224l-.008-.017c.008.11.02.202.037.29.054.27.161.488.419 1.003.288.578.235 1.15.076 1.629-.157.469-.422.867-.588 1.115l-.004.007a.25.25 0 1 1-.416-.278c.168-.252.4-.6.533-1.003.133-.396.163-.824-.049-1.246l-.013-.028c-.24-.48-.38-.758-.448-1.102a3 3 0 0 1-.052-.45l-.04.08a.25.25 0 1 1-.447-.224l.235-.468ZM6.013 2.06c-.649-.18-1.483.083-1.85.798-.131.258-.245.689-.08 1.335.063.244.414.198.487-.043.21-.697.627-1.447 1.359-1.692.217-.073.304-.337.084-.398"/></svg>' , blank=True, null=True)

    url = models.CharField(max_length=100,  default="", blank=True, null=True)
    is_active = models.BooleanField(default=True,  blank=True, null=True)
    def __str__(self):
        return self.name

class OpcionsConfiguration(models.Model):
    configuration = models.ForeignKey(ConfigurationCompany, on_delete=models.CASCADE, related_name="options_configuration")
    name = models.CharField(max_length=100, default="Opcion")
    is_checked = models.BooleanField(default=False, blank=True, null=True)
    input_text = models.CharField(max_length=255, default="", blank=True, null=True)
    url = models.CharField(max_length=100, default="", blank=True, null=True)

    OPTIONS = [(str(i), str(i)) for i in range(51)]
    select_option = models.CharField(max_length=2, choices=OPTIONS, default='0')

    def __str__(self):
        return f'{self.configuration.name} de {self.name}'