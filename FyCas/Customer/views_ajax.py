from . import models
from . import forms
from django.http import JsonResponse
from datetime import datetime
from twilio.rest import Client  
import time
from .mixing import Options
from num2words import num2words
from django.contrib.humanize.templatetags.humanize import intcomma


def SearchCustomer(request):
      list_cutomers = []
      for c in models.Customer.objects.all():
            dict_customer = { 
                    'id': c.id,
                    'filter':    c.name + " " + c.last_name + c.dni + c.calle_numero + "," + c.municipio +  ',' + c.sector +  ',' + c.ciudad +  c.work_information + c.number,
                    'name': c.name + " " + c.last_name,
                    "dni": c.dni,
                    "ubication": c.calle_numero + "," + c.municipio +  ',' + c.sector +  ',' + c.ciudad, 
                    "inf": c.work_information,
                    "refers": c.name_r1 + " " + " " + str(c.number_r1) + " - " + c.name_r2 + " " + str(c.number_r2) ,
                    "recide": c.address,
            }
            list_cutomers.append(dict_customer)
      return JsonResponse(list_cutomers,  safe=False)


def CustomerVerify(request):
        # cus = models.Customer.objects.all()
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.customer_verify == False:
            c.customer_verify = True
        c.save()
        print(c.customer_verify)
        # for cm in cus:
        #     cm.customer_verify = False 
        #     cm.save()
        return JsonResponse(list(),  safe=False)
    
def CustomerNoVerify(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.customer_verify == True:
            c.customer_verify = False
        c.save()
        return JsonResponse(list(),  safe=False)
    


def TurnDebeit(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.debit_visit == False:
            c.debit_visit = True
        else:
            c.debit_visit = False
        c.save()
        return JsonResponse(list(),  safe=False)    
    
def TurnDebeitFollow(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.debit_follow == False:
            c.debit_follow = True
        else:
            c.debit_follow = False
        c.save()
        return JsonResponse(list(),  safe=False)    
    
def TurnDebeitActive(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.debit == False:
            c.debit = True
        else:
            c.debit = False
        c.save()
        return JsonResponse(list(),  safe=False)    
    
def DisableCustomer(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.is_active == False:
            c.is_active = True
        else:
            c.is_active = False
        c.save()
        return JsonResponse(list(),  safe=False)    
    
    
def MensajeCustomerDebit(request):
        customer_debit = models.CustomerDebit.objects.filter(debit = True)
        for cb in customer_debit:
            print(f'Recordatorio enviado a: {cb.name}, {cb.number}')
            Send_WhatsApp_Message(cb.name, cb.number)
            time.sleep(20) 
            
        def Send_WhatsApp_Message(name, number):
            account_sid = 'AC32b5e94ce632aabd0a278a56e16bd44a'
            auth_token = 'a61c8b622e93ada5958d69dacef7c461'
            client = Client(account_sid, auth_token)

            Msm = f"Recordatorio de Pago - Grupo FyCas \n \nEstimado {name}: \n\nPor medio del presente mensaje, le recordamos que tiene una cuota pendiente. Su puntualidad en los pagos es muy importante para nosotros, por lo que le solicitamos amablemente que realice su pago lo antes posible. \n \nSi ya ha realizado su pago, por favor ignore este mensaje."
            message = client.messages.create(
                  body= Msm,
                  from_= '+13344384583',
                  to= f'+1{number}' )
            return True
        
        return JsonResponse(list(),  safe=False)    
    
    

def CreateCreditAjax(request):
        from datetime import datetime

        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        print(c, 'soy yo')
        credit = models.Credit.objects.create( 
            customer = c,
            dni = c.dni,
            name = c.name + " " + c.last_name,
            amount= int(request.GET.get('monto')),
            amount_feed = request.GET.get('monto_pagar'),
            no_account = int(0),
            price_feed = request.GET.get('cuotas'),
            day_pay = int(request.GET.get('dia')),
            mont = Options.MontNow(),
            day = Options.GetDayWeek(),
            day_number =  datetime.now().day,
            year = num2words(datetime.now().year, lang='es'),
            year_number = datetime.now().year,
        )
        c.monto_requerido =  intcomma(int(request.GET.get('monto')))
        c.save()
        print(num2words(datetime.now().year))
        data = {'monto_requerido':  intcomma(credit.amount)}
        return JsonResponse(data,  safe=False)    
    
    
def AplicarPago(request):
    cu = models.Cuota.objects.get(id=request.GET.get('id'))
    cu_ta = models.Cuota.objects.get(id=request.GET.get('id'))
    # print(request.GET.get('input'), 'soii')
    credit = models.Credit.objects.get(id=cu.credito.id)
    cuotas_o =  credit.credito.all()
    p_x_c = 1
    c_p = 0

    for cuo in cuotas_o:
        p_x_c += cu.cuota
        if cuo.abonado > 0:
            c_p += cuo.abonado
    print(c_p, 'siuuu')
    if  cu.estado == False:
        if cu.cuota != cu.abonado:
            monto_abonado = int(request.GET.get('input'))
            cu.abonado += monto_abonado
            cu.restante = max(cu.cuota - cu.abonado, 0)

            if cu.abonado >= cu.cuota:
                cu.abonado = cu.cuota


            if cu.cuota == cu.abonado:
                cu.estado = True
                cu.last_time_pay = datetime.now()
                
                credit.save()   
            cu.save()
        else:
            # Cuota pagada
            cu.estado = True
            cu.save()
            
    else:
        cu.estado = False
        cu.credito.estado = False
        # cu.save()

    customer_exist_credit = models.Customer.objects.get(id=credit.customer.id)

    # si exite una cuota con el estado false, este credito aun no ha sido saldado
    cuotas_credits_all = models.Cuota.objects.filter(credito__id=credit.id, estado=False).exists()
    if cuotas_credits_all == False:
        credit.estado_credito = True
        credit.save()

    

    D = {
        'id': cu_ta.id
    }
    Options().RunCreditValidate()
    return JsonResponse(D,  safe=False)    


def DeleteCreditAjax(request):
    credit_id = request.GET.get('id')
    try:
        credit = models.Credit.objects.get(id=int(credit_id))
        credit.delete()
        return JsonResponse({'status': 'success'}, safe=False)
    except models.Credit.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Credit not found'}, safe=False)


def CalcularMora(request):

    cuota = models.Cuota.objects.get(id=int(request.GET.get('id')))

    today = datetime.now().date()
    end_date =  cuota.end_date 
    days_late = (today - end_date).days





    print(cuota.cuota * 0.05, 'Dias de atraso con' , days_late )


    return JsonResponse( {'s':0}, safe=False)




def UploadImageURL(request):
            customer_id = request.GET.get('customer_id')
            image_url = request.FILES.get('image')

            bg_enfasis = request.POST.get('bg_enfasis')

    

            print(bg_enfasis, 'vamos a ver')
            company = models.Company.objects.get(user=request.user)
            company.Icon = image_url
            company.bg_enfasis = bg_enfasis
            company.save()
            return JsonResponse({'status': 'success'}, safe=False)
 

            return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, safe=False)

<<<<<<< HEAD






    




import openai

def ChatGPT(request):
        company = models.Company.objects.get(user=request.user)

        openai.api_key = company.key
        creditos = models.Credit.objects.filter(company=company, is_active = True)
        clientes = models.Customer.objects.filter(
            is_active=True, company=company)


        customer_list = []
        for customer in clientes:
            customer_info = {
            'name': customer.name + " " + customer.last_name,
            'number': customer.number,
            'ubication': customer.calle_numero + "," + customer.municipio + ',' + customer.sector + ',' + customer.ciudad,
            'refers': customer.name_r1 + " " + str(customer.number_r1) + " - " + customer.name_r2 + " " + str(customer.number_r2),
            'dni': customer.dni,
            'date': customer.day_created,


            'credito': list(customer.credit.all()) if customer.credit.all().exists() else None,
            'creditos': [
                {
                    'id': credito.id,
                    'amount': credito.amount,
                    'credito_atrasado': credito.credito_atrasado,
                }
                for credito in customer.credit.all()
            ] if customer.credit.all().exists() else None


            }
            customer_list.append(customer_info)

        total_inversion = 0
        for credito in creditos:
            total_inversion += credito.amount
        # Mensaje que envías al modelo
        mensaje = request.GET.get('message')
        prompt_sistema = f"""
        Eres un asistente especializado en finanzas creado para {company.name} Tu tarea principal es gestionar la información financiera de la empresa, te llamaras 

        Siempre mantén actualizada esta información clave:
        0.Te llamas Soli
        1. Número total de clientes activos: {clientes.count()}.
        2. Cantidad de créditos otorgados: {creditos.count()}.
        3. Ingresos totales de la empresa: 384,333.
        4. Inversion totale de la empresa: {total_inversion}
        5.Litado de clientes: {models.Customer.objects.filter(is_active=True, company=company)}
        6. Infomacion de clientes todas {models.Customer.objects.filter(is_active=True, company=company)}
        7. Informacion de clientes {customer_list}
        Reglas:
        - Proporciona respuestas claras, precisas y basadas en los datos que tienes disponibles.
       
        """

        try:
            respuesta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": mensaje}
                ]
            )
            contenido = respuesta["choices"][0]["message"]["content"]
            print(contenido)  # Muestra la respuesta en consola
            list_cutomers = []

            dictci = { 
                'response': contenido,
                }

            return JsonResponse(dictci,  safe=False)

        except Exception as e:
            print("Oh!", e)  # Imprime el error si ocurre
            list_cutomers = []

            dict_customer = { 
                'id': 1,
                }
            list_cutomers.append(dict_customer)
            return JsonResponse(list_cutomers,  safe=False)



  




    
""""
from django.shortcuts import render
from .models import Contacto
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

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
