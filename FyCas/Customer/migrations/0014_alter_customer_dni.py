# Generated by Django 5.0.3 on 2024-03-11 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0013_alter_customer_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dni',
            field=models.CharField(max_length=100),
        ),
    ]