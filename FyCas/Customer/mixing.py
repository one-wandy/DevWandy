from django.shortcuts import redirect
from django.urls import reverse
from . import models
import os
import copy
from num2words import num2words
from xhtml2pdf import pisa
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template
from django.template import Context


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
            year = {
            2023: "dos mil veintitrés",
            2024: "dos mil veinticuatro",
            2025: "dos mil veinticinco",
            2026: "dos mil veintiséis",
            2027: "dos mil veintisiete",
            2028: "dos mil veintiocho",
            2029: "dos mil veintinueve",
            2030: "dos mil treinta",
            2031: "dos mil treinta y uno",
            2032: "dos mil treinta y dos",
            2033: "dos mil treinta y tres",
            2034: "dos mil treinta y cuatro",
            2035: "dos mil treinta y cinco",
            2036: "dos mil treinta y seis",
            2037: "dos mil treinta y siete",
            2038: "dos mil treinta y ocho",
            2039: "dos mil treinta y nueve",
            2040: "dos mil cuarenta"
      }
            return year.get(N)
      
      def Amount(self, N):
            amount = {
                  10000: "diez mil",
                  15000: "quince mil",
                  20000: "veinte mil",
                  25000: "veinticinco mil",
                  30000: "treinta mil",
                  35000: "treinta y cinco mil",
                  40000: "cuarenta mil",
                  45000: "cuarenta y cinco mil",
                  50000: "cincuenta mil",
                  55000: "cincuenta y cinco mil",
                  60000: "sesenta mil",
                  65000: "sesenta y cinco mil",
                  70000: "setenta mil",
                  75000: "setenta y cinco mil",
                  80000: "ochenta mil",
                  85000: "ochenta y cinco mil",
                  90000: "noventa mil",
                  95000: "noventa y cinco mil",
                  # $100,0000 Cien Mil
                  100000: "cien mil",
                  105000: "ciento cinco mil",
                  110000: "ciento diez mil",
                  115000: "ciento quince mil",
                  120000: "ciento veinte mil",
                  125000: "ciento veinticinco mil",
                  130000: "ciento treinta mil",
                  135000: "ciento treinta y cinco mil",
                  140000: "ciento cuarenta mil",
                  145000: "ciento cuarenta y cinco mil",
                  150000: "ciento cincuenta mil",
                  155000: "ciento cincuenta y cinco mil",
                  160000: "ciento sesenta mil",
                  165000: "ciento sesenta y cinco mil",
                  170000: "ciento setenta mil",
                  175000: "ciento setenta y cinco mil",
                  180000: "ciento ochenta mil",
                  185000: "ciento ochenta y cinco mil",
                  190000: "ciento noventa mil"     ,
                  995000: "novecientos noventa y cinco mil",
                  
                  # $200,000.00 - Doscientos Mil
                  200000: "doscientos mil",
                  205000: "doscientos cinco mil",
                  210000: "doscientos diez mil",
                  215000: "doscientos quince mil",
                  220000: "doscientos veinte mil",
                  225000: "doscientos veinticinco mil",
                  230000: "doscientos treinta mil",
                  235000: "doscientos treinta y cinco mil",
                  240000: "doscientos cuarenta mil",
                  245000: "doscientos cuarenta y cinco mil",
                  250000: "doscientos cincuenta mil",
                  255000: "doscientos cincuenta y cinco mil",
                  260000: "doscientos sesenta mil",
                  265000: "doscientos sesenta y cinco mil",
                  270000: "doscientos setenta mil",
                  275000: "doscientos setenta y cinco mil",
                  280000: "doscientos ochenta mil",
                  285000: "doscientos ochenta y cinco mil",
                  290000: "doscientos noventa mil",
                  295000: "doscientos noventa y cinco mil",
                  
                  #$300,000 Trescientos Mil
                  300000: "trescientos mil",
                  305000: "trescientos cinco mil",
                  310000: "trescientos diez mil",
                  315000: "trescientos quince mil",
                  320000: "trescientos veinte mil",
                  325000: "trescientos veinticinco mil",
                  330000: "trescientos treinta mil",
                  335000: "trescientos treinta y cinco mil",
                  340000: "trescientos cuarenta mil",
                  345000: "trescientos cuarenta y cinco mil",
                  350000: "trescientos cincuenta mil",
                  355000: "trescientos cincuenta y cinco mil",
                  360000: "trescientos sesenta mil",
                  365000: "trescientos sesenta y cinco mil",
                  370000: "trescientos setenta mil",
                  375000: "trescientos setenta y cinco mil",
                  380000: "trescientos ochenta mil",
                  385000: "trescientos ochenta y cinco mil",
                  390000: "trescientos noventa mil",
                  395000: "trescientos noventa y cinco mil",
                  
                  #$ 400,000 Cuatrocientos Mil
                  400000: "cuatrocientos mil",
                  405000: "cuatrocientos cinco mil",
                  410000: "cuatrocientos diez mil",
                  415000: "cuatrocientos quince mil",
                  420000: "cuatrocientos veinte mil",
                  425000: "cuatrocientos veinticinco mil",
                  430000: "cuatrocientos treinta mil",
                  435000: "cuatrocientos treinta y cinco mil",
                  440000: "cuatrocientos cuarenta mil",
                  445000: "cuatrocientos cuarenta y cinco mil",
                  450000: "cuatrocientos cincuenta mil",
                  455000: "cuatrocientos cincuenta y cinco mil",
                  460000: "cuatrocientos sesenta mil",
                  465000: "cuatrocientos sesenta y cinco mil",
                  470000: "cuatrocientos setenta mil",
                  475000: "cuatrocientos setenta y cinco mil",
                  480000: "cuatrocientos ochenta mil",
                  485000: "cuatrocientos ochenta y cinco mil",
                  490000: "cuatrocientos noventa mil",
                  495000: "cuatrocientos noventa y cinco mil",
                  
                  #$500,000 Quinientos Mil
                  500000: "quinientos mil",
                  505000: "quinientos cinco mil",
                  510000: "quinientos diez mil",
                  515000: "quinientos quince mil",
                  520000: "quinientos veinte mil",
                  525000: "quinientos veinticinco mil",
                  530000: "quinientos treinta mil",
                  535000: "quinientos treinta y cinco mil",
                  540000: "quinientos cuarenta mil",
                  545000: "quinientos cuarenta y cinco mil",
                  550000: "quinientos cincuenta mil",
                  555000: "quinientos cincuenta y cinco mil",
                  560000: "quinientos sesenta mil",
                  565000: "quinientos sesenta y cinco mil",
                  570000: "quinientos setenta mil",
                  575000: "quinientos setenta y cinco mil",
                  580000: "quinientos ochenta mil",
                  585000: "quinientos ochenta y cinco mil",
                  590000: "quinientos noventa mil",
                  595000: "quinientos noventa y cinco mil",
                  600000: "seiscientos mil",
                  
                  600000: "seiscientos mil",
                  605000: "seiscientos cinco mil",
                  610000: "seiscientos diez mil",
                  615000: "seiscientos quince mil",
                  620000: "seiscientos veinte mil",
                  625000: "seiscientos veinticinco mil",
                  630000: "seiscientos treinta mil",
                  635000: "seiscientos treinta y cinco mil",
                  640000: "seiscientos cuarenta mil",
                  645000: "seiscientos cuarenta y cinco mil",
                  650000: "seiscientos cincuenta mil",
                  655000: "seiscientos cincuenta y cinco mil",
                  660000: "seiscientos sesenta mil",
                  665000: "seiscientos sesenta y cinco mil",
                  670000: "seiscientos setenta mil",
                  675000: "seiscientos setenta y cinco mil",
                  680000: "seiscientos ochenta mil",
                  685000: "seiscientos ochenta y cinco mil",
                  690000: "seiscientos noventa mil",
                  695000: "seiscientos noventa y cinco mil",
                  
                  700000: "setecientos mil",
                  705000: "setecientos cinco mil",
                  710000: "setecientos diez mil",
                  715000: "setecientos quince mil",
                  720000: "setecientos veinte mil",
                  725000: "setecientos veinticinco mil",
                  730000: "setecientos treinta mil",
                  735000: "setecientos treinta y cinco mil",
                  740000: "setecientos cuarenta mil",
                  745000: "setecientos cuarenta y cinco mil",
                  750000: "setecientos cincuenta mil",
                  755000: "setecientos cincuenta y cinco mil",
                  760000: "setecientos sesenta mil",
                  765000: "setecientos sesenta y cinco mil",
                  770000: "setecientos setenta mil",
                  775000: "setecientos setenta y cinco mil",
                  780000: "setecientos ochenta mil",
                  785000: "setecientos ochenta y cinco mil",
                  790000: "setecientos noventa mil",
                  795000: "setecientos noventa y cinco mil",
                  800000: "ochocientos mil",
                  805000: "ochocientos cinco mil",
                  810000: "ochocientos diez mil",
                  815000: "ochocientos quince mil",
                  820000: "ochocientos veinte mil",
                  825000: "ochocientos veinticinco mil",
                  830000: "ochocientos treinta mil",
                  835000: "ochocientos treinta y cinco mil",
                  840000: "ochocientos cuarenta mil",
                  845000: "ochocientos cuarenta y cinco mil",
                  850000: "ochocientos cincuenta mil",
                  855000: "ochocientos cincuenta y cinco mil",
                  860000: "ochocientos sesenta mil",
                  865000: "ochocientos sesenta y cinco mil",
                  870000: "ochocientos setenta mil",
                  875000: "ochocientos setenta y cinco mil",
                  880000: "ochocientos ochenta mil",
                  885000: "ochocientos ochenta y cinco mil",
                  895000: "ochocientos noventa y cinco mil",
                  
                  900000: "novecientos mil",
                  905000: "novecientos cinco mil",
                  910000: "novecientos diez mil",
                  915000: "novecientos quince mil",
                  920000: "novecientos veinte mil",
                  925000: "novecientos veinticinco mil",
                  930000: "novecientos treinta mil",
                  935000: "novecientos treinta y cinco mil",
                  940000: "novecientos cuarenta mil",
                  945000: "novecientos cuarenta y cinco mil",
                  950000: "novecientos cincuenta mil",
                  955000: "novecientos cincuenta y cinco mil",
                  960000: "novecientos sesenta mil",
                  965000: "novecientos sesenta y cinco mil",
                  970000: "novecientos setenta mil",
                  975000: "novecientos setenta y cinco mil",
                  980000: "novecientos ochenta mil",
                  985000: "novecientos ochenta y cinco mil",
                  990000: "novecientos noventa mil",
                  995000: "novecientos noventa y cinco mil",
                  
                  1000000: "un millón",
            }
            return amount.get(N)


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
