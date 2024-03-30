import os
import copy
from . import models
from xhtml2pdf import pisa
from datetime import datetime
from django.urls import reverse
from num2words import num2words
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template


class Options:
      def List_Credit(self):
            URL = reverse('customer:list-credit')
            return redirect(URL)
      
      def List_Redirect(self):
            URL = reverse('customer:list-customer')
            return redirect(URL)
      
      def UpdateCredit(self, credit_id):
            URL = reverse('customer:update-credit',  kwargs={'pk': credit_id})
            return redirect(URL)
      
      def CreateCredit(self, credit_id):
            URL = reverse('customer:create-credit',  kwargs={'pk': credit_id})
            return redirect(URL)
      
      def FileCreate(self, Name, Last):
            path = os.getcwd() + "\Clientes"
            name_file = Name + " " + Last
            sub_file = os.path.join(path, name_file)
            try:
                  os.mkdir(sub_file)
                  return True
            except FileExistsError: 
                  return False

      def PDF(self, html_file, pdf_file ):
            # Opciones de configuración para pdfkit (opcional)
            options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            }

            # Convertir HTML a PDF
            pdfkit.from_file(html_file, pdf_file, options=options)

            print(f'Se ha generado el archivo PDF: {pdf_file}')
            
      def DayNow(self, N):
            day = {
        1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
        6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez",
        11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
        16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve", 20: "veinte",
        21: "veintiuno", 22: "veintidós", 23: "veintitrés", 24: "veinticuatro", 25: "veinticinco",
        26: "veintiséis", 27: "veintisiete", 28: "veintiocho", 29: "veintinueve", 30: "treinta",
        31: "treinta y uno"
            }
            return day.get(N)

      def MontNow(self, N):
            mont = {
        1: "enero",     2: "febrero",   3: "marzo",    4: "abril", 5: "mayo",
        6: "junio", 7: "julio", 8: "agosto",    9: "septiembre",
        10: "octubre",  11: "noviembre",  12: "diciembre"
        }
            return mont.get(N)

      def YearNow(self, N):
            return num2words(N, lang='es')
      
      def Amount(self, N):
            return num2words(N, lang='es')

      def Count(self, N):
            return num2words(N, lang='es')
      
      def CreatePdf(self, template, name):

            """
            Función para generar un PDF a partir de una plantilla HTML.
            Parámetros:
                  request: La solicitud HTTP.
                  template: La ruta de la plantilla HTML.
                  filename: El nombre del archivo PDF.

            Retorno:
                  Un objeto HttpResponse con el contenido del PDF.
            """

            # Renderizar la plantilla
            template = get_template(template)
            html = template.render()
            # Crear el objeto HttpResponse con el contenido generado
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{name}.pdf"'

            # Convertir HTML a PDF
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                  return HttpResponse('Error al generar PDF', status=500)

            return response
