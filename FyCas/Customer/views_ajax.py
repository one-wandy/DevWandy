from . import models
from . import forms
from django.http import JsonResponse


# Buscar Clientes 
def SearchCustomer(request):
      list_cutomers = []
      for c in models.Customer.objects.all():
            dict_customer = { 
                'name': c.name + " " + c.last_name,
                "dni": c.dni,
                "img": c.img1.url,
                "inf": c.work_information,
                "refers": c.name_r1 + " " + " " + str(c.number_r1) + " - " + c.name_r2 + " " + str(c.number_r2) ,
                "recide": c.address,
            }
            list_cutomers.append(dict_customer)
      return JsonResponse(list_cutomers,  safe=False)


