# Generated by Django 5.0 on 2024-11-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_cuota_dias_en_atraso'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='Icon_img',
            field=models.ImageField(blank=True, default='media/img-default/img.png', null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='company',
            name='contrato',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='notarial',
            field=models.TextField(blank=True),
        ),
    ]
