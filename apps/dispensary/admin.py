from django.contrib import admin
from apps.dispensary.models import Pharmacy, Prescription, Medicine, Invoice, Vaccine, Country, Order

# Register your models here.

admin.site.register(Pharmacy)
admin.site.register(Prescription)
admin.site.register(Medicine)
admin.site.register(Invoice)
admin.site.register(Vaccine)
admin.site.register(Country)
admin.site.register(Order)
