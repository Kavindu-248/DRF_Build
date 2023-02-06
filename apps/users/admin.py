from django.contrib import admin
from apps.users.models import User, Patient, Doctor, PharmacyUser


admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PharmacyUser)
