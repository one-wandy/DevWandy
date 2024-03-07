from django import forms
from . import models  # Asegúrate de importar correctamente el modelo

class CustomerForm(forms.ModelForm):
    class Meta:
      model = models.Customer
      fields = ['name', 'last_name', 'number', 'address', 'email', 'amount_purpose', 'work_information', 'references_peopple', 'dni']

      widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'amount_purpose': forms.Textarea(attrs={'class': 'form-control'}),
            'work_information': forms.Textarea(attrs={'class': 'form-control'}),
            'references_peopple': forms.Textarea(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
        }