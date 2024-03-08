from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, default="Anonimo")
    last_name = models.CharField(max_length=255)
    number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    amount_purpose = models.TextField(max_length=355)
    work_information = models.TextField(max_length=300)
    references_peopple = models.TextField(max_length=500)
    dni = models.IntegerField(default=000000000000)
    amount = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name
