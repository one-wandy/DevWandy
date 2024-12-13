from django.contrib import admin
from .models import  Customer, Credit, Company, PayCredit, Img, CustomerDebit, Cuota, ConfigurationCompany, OpcionsConfiguration, Category

admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Credit)
admin.site.register(PayCredit)
admin.site.register(Img)
admin.site.register(CustomerDebit)
admin.site.register(Cuota)
admin.site.register(ConfigurationCompany)
admin.site.register(OpcionsConfiguration)
admin.site.register(Category)
