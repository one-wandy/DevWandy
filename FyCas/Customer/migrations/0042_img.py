# Generated by Django 5.0 on 2024-05-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0041_customer_customer_verify'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Money', max_length=233)),
                ('Icon', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
