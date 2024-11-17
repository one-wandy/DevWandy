# Generated by Django 5.0 on 2024-11-17 00:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0072_settingapp_bg_enfasis'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Grupo Fycas', max_length=233)),
                ('Icon', models.ImageField(blank=True, default='media/img-default/img.png', null=True, upload_to='media/')),
                ('bg_enfasis', models.CharField(blank=True, default='rgb(83, 137, 255)', max_length=233)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OptionModulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('url', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='Customer.modulo')),
            ],
        ),
        migrations.DeleteModel(
            name='SettingApp',
        ),
    ]
