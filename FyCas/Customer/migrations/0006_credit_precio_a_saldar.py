# Generated by Django 5.0 on 2024-11-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0005_credit_capital_no_variable'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='precio_a_saldar',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
