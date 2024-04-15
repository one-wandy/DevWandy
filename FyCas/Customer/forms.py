from django import forms
from . import models  # Asegúrate de importar correctamente el modelo

class CustomerForm(forms.ModelForm):
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aquí puedes asignar la clase CSS a todos los campos
        # widgets = { 
              # "img1": forms.FileInput(attrs={'class': 'img1'}),
            #  "img2": forms.FileInput(attrs={'class': 'img2'})
      # }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
        
    class Meta:
      model = models.Customer
      fields = ['name', 'last_name', 'number', 'address',  'work_information',  'dni',  "img2", "img1", "name_r1", "name_r2", "number_r1", "number_r2",
        'lat', 'lon',
    # Datos personales
    'type_input',
    'sexo',
    'estado_civil',
    'ocupacion',
    'code_customer',
    'nacimiento',
    'nacionalidad',
    'direccion',
    'sector',
    'calle_numero',
    'municipio',
    'ciudad',
    'provincia',
    'pais',
    'dir_referencia',
    'phone',
    
    # # Datos de trabajo
    'empresa_trabaja',
    'cargo',
    'direccion_trabajo',
    'sector',  # Renombrado para evitar conflicto de nombres
    'calle_numero_trabajo',
    'municipio_trabaja',
    'ciudad_trabaja',
    'provincia_trabajo',
    'pais_trabajo',
    'dir_referencia_trabajo',
    'salario_m',
    'moneda',
    
    'relacion_tipo',
    'fecha_apertura',
    'fecha_vencimiento',
    'fecha_ultimo_pago',
    'numeoro_cuenta',  # Corregido de 'numeoro_cuenta'
    'estatus',
    'tipo_prestamo',
    'moneda_prestamo',
    'credito_aprovado',  # Corregido de 'credito_aprovado'
    'balance_corte',
    'monto_adeudado',
    'pago_mandatorio_cuota',
    'monto_ultimo_pago',
    'total_atraso',
    'tasa_interes',
    'forma_pago',
    'cantidad_cuota',
    'atraso1_30',
    'atraso31_60',
    'atraso61_90',
    'atraso91_120',
    'atraso121_150',
    'atraso151_180',
    'atraso181_o_mas'
    
    ]


      #       'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nombre Completo"}),
      #       'last_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Apellidos" }),
            
      #       'name_r1': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nombre" }),
            
      #       'name_r2': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Apellidos" }),
            
      #       'number': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            
      #       'number_r1': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            
      #       'number_r2': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            
      #       'address': forms.TextInput(attrs={'class': 'form-control address', "placeholder": "Donde Recide"}),
       
      #       'work_information': forms.Textarea(attrs={'class': 'form-control textarea', "placeholder": "Informacion Laboral"}),

      #       'dni': forms.TextInput(attrs={'class': 'form-control',  "placeholder": "232-3232-3232", }),

      #   }
      
      
class CreditForm(forms.ModelForm):
  class Meta:
      model = models.Credit
      fields = [
        "customer", "name", "price_feed", "no_account", 
         "mode_pay", "day_pay", "dni", "amount", "amount_feed",
      ]
      widgets = {
        'customer': forms.TextInput(attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'dni': forms.TextInput(attrs={'class': 'form-control'}),
        'amount': forms.NumberInput(attrs={'class': 'form-control'}),

        'price_feed': forms.NumberInput(attrs={'class': 'form-control'}),
        'no_account': forms.TextInput(attrs={'class': 'form-control'}),
        'day_pay': forms.NumberInput(attrs={'class': 'form-control'}),
        'amount_feed': forms.TextInput(attrs={'class': 'form-control'}),

      }