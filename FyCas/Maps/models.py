from django.db import models

# Create your models here.
class Credentials(models.Model):
      client_id = models.CharField(max_length=300, default='', blank=True)
      client_secret = models.CharField(max_length=300, default='', blank=True)
      scopes = models.CharField(max_length=300, default='', blank=True)
      
      def __str__(self):
            return self.client_id
      
      