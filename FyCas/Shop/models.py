from django.db import models
from Customer.models import Company
# Create your models here.


from django.db import models

class Sale(models.Model):
      company= models.ForeignKey(Company, on_delete=models.CASCADE,  blank=True, null=True, related_name="sale_company")
      name = models.CharField(max_length=255, blank=True, null=True, default='Venta#')  # Nombre de la venta (puede ser el nombre del cliente o un código)
      total = models.DecimalField(max_digits=10, decimal_places=2)  # Total de la venta
      discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Descuento aplicado (si hay)

      def __str__(self):
            return f"Venta: {self.name}, Total: RD$ {self.total}"



class Categori(models.Model):
      company= models.ForeignKey(Company, on_delete=models.CASCADE,  blank=True, null=True, related_name="categori_company")
      name = models.CharField(max_length=255, blank=True, null=True, default='Categoria 1') 
      img = models.ImageField(upload_to='media/categori/', blank=True, null=True) 
      
      def __str__(self):
            return f"Categoria: {self.name}"



class Item(models.Model):
      company= models.ForeignKey(Company, on_delete=models.CASCADE,  blank=True, null=True, related_name="item_company")
      name = models.CharField(max_length=255, blank=True, null=True, default='Articulo')  # Nombre del artículo
      price = models.DecimalField(max_digits=10, decimal_places=2,)  # Precio del artículo
      img = models.ImageField(upload_to='media/item/', blank=True, null=True)  # Imagen del artículo
      discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Descuento aplicado al artículo
      stock = models.IntegerField(default=0)  # Stock disponible
      unit_of_measurement = models.CharField(max_length=50)  # Unidad de medida (ej. pieza, kg, etc.)

      def __str__(self):
            return f"Item: {self.name}, Precio: RD$ {self.price}, Stock: {self.stock}"

