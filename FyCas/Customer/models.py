from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    # Para el tema de las solicitudes, cuando el user ingresa por primera vez el estado permanece false durante los proximos 7 dias, sera descartado y eliminado de la base de datos ya que su aprobacion no fue verificada por lo tanto no cambio a " True " pero se guardada su DNI en una base de datos adicional mas adelante p
    not_aprobado = models.BooleanField(default=False,  blank=True)
    # Si 
    customer_verify = models.BooleanField(default=True,  blank=True)
    
    debit = models.BooleanField(default=False,  blank=True)
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
    company = models.CharField(max_length=255, default='Grupo Fycas', blank=True )
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
    img1 = models.ImageField(upload_to="media/",  blank=True, null=True, default="media/img-default/img.png")#Foto de Cedula delantera
    img2 = models.ImageField(upload_to="media/", blank=True, null=True, default="media/img-default/img.png")#Foto de Cedula tracera
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
        return self.name


class Credit(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE, related_name="credit")
    amount = models.IntegerField(default=10000)
    name = models.CharField(max_length=100)
    price_feed = models.IntegerField(default=1)
    dni = models.TextField(default="")
    no_account = models.TextField() #Numero de Cuenta
    
    #thow pay for monts
    mode_pay = models.BooleanField(default=False)
    #if mode_pay is True Appli 2 Pay 
    day_pay = models.IntegerField(default=30)
    is_active = models.BooleanField(default=True)#is active rederict at diferens view

    # 
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
    
    
    def __str__(self):
        return self.name


class PayCredit(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="media/", blank=True, null=True, default="") 
    


    
class SettingApp(models.Model):
    name = models.CharField(blank=True, max_length=233, default='Grupo Fycas')
    Icon = models.ImageField(upload_to="media/", blank=True, null=True, default="media/img-default/img.png") #Foto de Cedula tracera
    
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