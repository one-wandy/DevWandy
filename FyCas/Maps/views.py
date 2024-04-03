import os
from . import models
from django.views.generic import *
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from Customer.mixing import Options
from datetime import datetime
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from fpdf import FPDF
from django.http import JsonResponse
from twilio.rest import Client  

class Maps(TemplateView, Options):
      template_name = "maps/information.html"

      
      
      def get(self, request, *args, **kwargs):
            nombre_archivo = "Info.docx"
            ruta_carpeta =  os.getcwd() + "\Clientes"
            self.send_whatsapp_message("+18295577196","+18098707852")
            return super().get(request, *args, **kwargs)
      

      def send_whatsapp_message(self, from_number, to_number):
            """
            Sends a WhatsApp message using Twilio.

            Args:
                  from_number: The Twilio phone number in the format "whatsapp:+1..." (sender).
                  to_number: The recipient's phone number in the format "whatsapp:+1..." (receiver).

            Returns:
                  A JsonResponse containing the message ID if successful, otherwise an error message.
            """
            account_sid = 'AC32b5e94ce632aabd0a278a56e16bd44a'
            auth_token = 'a61c8b622e93ada5958d69dacef7c461'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                  body='¡Hola! Este es un mensaje de prueba desde Django.',
                  from_=from_number,
                  to=to_number
                  )
            return JsonResponse({'message_id': message.sid})
