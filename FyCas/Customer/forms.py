from django import forms
from . import models  # Asegúrate de importar correctamente el modelo

class CustomerForm(forms.ModelForm):
    class Meta:
      model = models.Customer
      fields = ['name', 'last_name', 'number', 'address', 'email', 'amount_purpose', 'work_information', 'references_peopple', 'dni', "amount", "img2", "img1"]

      widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nombre Completo"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Apellidos" }),
            'number': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Cantidad"}),
            'address': forms.TextInput(attrs={'class': 'form-control address', "placeholder": "Donde Recide"}),
            'email': forms.EmailInput(attrs={'class': 'form-control' , "placeholder": "Correo"} ),
            'amount_purpose': forms.Textarea(attrs={'class': 'form-control textarea'}),
            'work_information': forms.Textarea(attrs={'class': 'form-control textarea', "placeholder": "Informacion Laboral"}),
            'references_peopple': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Personas Referentes"}),
            'dni': forms.NumberInput(attrs={'class': 'form-control',  "placeholder": "232-3232-3232"}),
            "img1": forms.FileInput(attrs={'class': 'img1'}),
             "img2": forms.FileInput(attrs={'class': 'img2'})
        }