from django.shortcuts import redirect
from django.urls import reverse
from . import models
import os
import copy


class Options:
      def List_Redirect(self):
            URL = reverse('customer:list-customer')
            return redirect(URL)
      
      def FileCreate(self, Name, Last):
            path = os.getcwd() + "\Clientes"
            name_file = Name + "-" + Last
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

