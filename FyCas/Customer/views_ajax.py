from . import models
from . import forms
from django.http import JsonResponse


# Buscar Clientes 
def SearchCustomer(request):
      list_cutomers = []
      for c in models.Customer.objects.all():
            dict_customer = { 
                  'id': c.id,
                  'name': c.name + " " + c.last_name,
                  "dni": c.dni,
                    "img": c.img1.url if c.img1 else None,              
                    "inf": c.work_information,
                  "refers": c.name_r1 + " " + " " + str(c.number_r1) + " - " + c.name_r2 + " " + str(c.number_r2) ,
                  "recide": c.address,
            }
            list_cutomers.append(dict_customer)
      return JsonResponse(list_cutomers,  safe=False)


""""
from django.shortcuts import render
from .models import Contacto
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def migrar_contactos(request):
    # Leer contactos de la base de datos
    contactos = Contacto.objects.all()

    # Transformar datos
    contactos_google = []
    for contacto in contactos:
        contacto_google = {
            "givenName": contacto.nombre,
            "familyName": contacto.apellido,
            "emails": [{"value": contacto.correo_electronico}],
            "phones": [{"value": contacto.numero_telefono}],
        }
        contactos_google.append(contacto_google)

    # Autenticarse con la API de Google Contacts
    credenciales = Credentials.from_service_account_file('credentials.json')
    cliente = build('people', 'v1', credentials=credenciales)

    # Crear o actualizar contactos en Google Contacts
    for contacto_google in contactos_google:
        persona = cliente.people().resource().create(body=contacto_google).execute()
        print(f"Contacto creado: {persona.resourceName}")

    return render(request, 'contacto/migracion_exitosa.html')

"""""
