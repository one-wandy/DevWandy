import os
from . import models
from django.views.generic import *
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from Customer.mixing import Options
from datetime import datetime
from django.template.loader import get_template
from weasyprint import HTML
from django.http import HttpResponseRedirect, HttpResponse
from fpdf import FPDF
class Maps(TemplateView, Options):
      template_name = "maps/information.html"

      
      
      def get(self, request, *args, **kwargs):
            nombre_archivo = "Info.docx"
            ruta_carpeta =  os.getcwd() + "\Clientes"
            self.render_to_pdf()
            return super().get(request, *args, **kwargs)
      

      def render_to_pdf(self, template_src, context_dict={}):
            template = get_template(template_src)
            html = template.render(context_dict)
            pdf = HTML(string=html).write_pdf()

            # Asegúrate de que el directorio 'cliente' exista
            if not os.path.exists('Cliente'):
                  os.makedirs('Cliente')

            # Define la ruta para el PDF
            pdf_path = os.path.join('cliente', 'output.pdf')

            # Guarda el PDF en el directorio 'cliente'
            with open(pdf_path, 'wb') as f:
                  f.write(pdf)

            # Devuelve la ruta donde se guardó el PDF
            return pdf_path
