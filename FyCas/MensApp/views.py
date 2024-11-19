from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from Customer.mixing import Options
from .mixing import enviar_respuesta, procesar_mensaje

class MensApp(TemplateView, Options):
    template_name = "mensapp/dashboard.html"
    
    def get_context_data(self, **kwargs):
        enviar_respuesta('Qloq Chamo', '+18295577196')
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()
        return context