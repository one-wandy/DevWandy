# Generated by Django 5.0 on 2024-11-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_company_icon_img_company_contrato_company_notarial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='capital_no_variable',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]