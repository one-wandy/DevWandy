from django.contrib import admin
from .models import  Customer, Credit, SettingApp, PayCredit, Img

admin.site.register(Customer)
admin.site.register(Credit)
admin.site.register(SettingApp)
admin.site.register(PayCredit)
admin.site.register(Img)

