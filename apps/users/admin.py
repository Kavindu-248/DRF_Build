from django.contrib import admin
from apps.users.models import User, Patient, Doctor, PharmacyUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PharmacyUser)
