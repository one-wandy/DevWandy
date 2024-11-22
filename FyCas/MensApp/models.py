from django.db import models

# Create your models here.
class Mens(models.Model):
      nombre = models.CharField(max_length=100)
      mensaje = models.TextField()
      fecha_creacion = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.nombre