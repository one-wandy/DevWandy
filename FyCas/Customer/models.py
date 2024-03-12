from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, )#Nombre
    last_name = models.CharField(max_length=255)#Apellido
    number = models.CharField(max_length=20, blank=True)#Numero local o Movile
    address = models.CharField(max_length=255)#Direccion de donde recide
    email = models.EmailField(null=True)#Correo electronico
    amount_purpose = models.TextField(max_length=355)#Proposito por el que se solicita el prestamo
    work_information = models.TextField(max_length=300)#Informacion donde trabaja
    references_peopple = models.TextField(max_length=500)#Personas referentes
    dni = models.CharField(max_length=100) #Numero de Identidad
    amount = models.IntegerField(null=True)#Monto 
    no_account = models.IntegerField(default=0) #Numero de Cuenta
    img1 = models.ImageField(upload_to="media/", blank=True, null=True)#Foto de Cedula delantera
    img2 = models.ImageField(upload_to="media/", blank=True, null=True)#Foto de Cedula tracera
    name_r1 = models.CharField(max_length=255,  )#Nombre
    name_r2 = models.CharField(max_length=255,  )#Nombre
    number_r1 = models.IntegerField( )#Numero local o Movile
    number_r2 = models.IntegerField( )#Numero local o Movile
    
    def __str__(self):
        return self.name


class Credit(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.IntegerField(default=10000)
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    no_account = models.IntegerField() #Numero de Cuenta
    
    #thow pay for monts
    mode_pay = models.BooleanField(default=False)
    #if mode_pay is True Appli 2 Pay 
    day_pay = models.IntegerField(default=30)
    day_pay2 = models.IntegerField(default=15)
