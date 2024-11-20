# Generated by Django 5.0 on 2024-11-17 22:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0088_remove_customer_company_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='rnc',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]