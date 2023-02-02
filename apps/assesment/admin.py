from django.contrib import admin
from apps.assesment.models import FormAssesment, SubscriptionForm, Answer, Avalability, Question, TreatmentType, Appointment

# Register your models here.

admin.site.register(FormAssesment)
admin.site.register(SubscriptionForm)
admin.site.register(Answer)
admin.site.register(Avalability)
admin.site.register(Question)
admin.site.register(TreatmentType)
admin.site.register(Appointment)
