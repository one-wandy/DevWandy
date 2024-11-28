from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from Customer.mixing import Options
# from .mixing import enviar_respuesta, procesar_mensaje

class Shop(TemplateView, Options):
    template_name = "shop/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()
        return context


class Inventario(TemplateView, Options):
    template_name = "shop/inventario.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.Company()
        return context