from django import forms
from . import models  # Asegúrate de importar correctamente el modelo

class CustomerForm(forms.ModelForm):
    class Meta:
      model = models.Customer
      fields = ['name', 'last_name', 'number', 'address',  'work_information',  'dni',  "img2", "img1", "name_r1", "name_r2", "number_r1", "number_r2"]

      widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nombre Completo"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Apellidos" }),
            
            'name_r1': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nombre" }),
            
            'name_r2': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Apellidos" }),
            
            'number': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            
            'number_r1': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            
            'number_r2': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            
            'address': forms.TextInput(attrs={'class': 'form-control address', "placeholder": "Donde Recide"}),
       
            'work_information': forms.Textarea(attrs={'class': 'form-control textarea', "placeholder": "Informacion Laboral"}),

            'dni': forms.TextInput(attrs={'class': 'form-control',  "placeholder": "232-3232-3232"}),
            "img1": forms.FileInput(attrs={'class': 'img1'}),
             "img2": forms.FileInput(attrs={'class': 'img2'})
        }
      
      
class CreditForm(forms.ModelForm):
  class Meta:
      model = models.Credit
      fields = [
        "customer", "name", "price_feed", "no_account", 
         "mode_pay", "day_pay", "day_pay2", "dni", "amount",
      ]
      widgets = {
        'customer': forms.TextInput(attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'dni': forms.TextInput(attrs={'class': 'form-control'}),
        'amount': forms.NumberInput(attrs={'class': 'form-control'}),

        'price_feed': forms.NumberInput(attrs={'class': 'form-control'}),
        'no_account': forms.TextInput(attrs={'class': 'form-control'}),
        'day_pay': forms.NumberInput(attrs={'class': 'form-control'}),
        'day_pay2': forms.NumberInput(attrs={'class': 'form-control'}),
      }