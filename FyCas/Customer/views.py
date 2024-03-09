from django.shortcuts import render
from django.views.generic import *
from . import forms
from . import models


class AddCustomer(CreateView):
    model = models.Customer
    form_class = forms.CustomerForm
    template_name = "customer/add-customer.html"
    
    def post(self, request, *args, **kwargs):
        
        self.model.objects.create(
            name =request.POST.get("name"),
            last_name = request.POST.get("last_name"),
            number =int(request.POST.get("number")),
            address =request.POST.get("address"),
            dni =int(request.POST.get("dni")),
            img1 =request.FILES.get("img1"),
            img2=request.FILES.get("img2"),
        )
        return super().post(request, *args, **kwargs)


    
    def get_success_url(self):
        # Redirigir a una URL específica después de guardar el formulario
        return reverse_lazy('mi_vista_de_exito')
    
class ListCustomer(ListView):
    model = models.Customer
    template_name = "customer/list-customer.html"
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = self.model.objects.all()
        return context