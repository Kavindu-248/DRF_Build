import datetime
from django.db import models

from apps.users.models import Patient, Doctor
from apps.files.models import File
from apps.dispensary.models import Prescription , Order


# Choice Fields


class TreatmentOption(models.TextChoices):

    DIABETES = 'DIABETES', ('DIABETES')
    CHOLESTREROL = 'CHOLESTREROL', ('CHOLESTREROL')
    HYPERTENSION = 'HYPERTENSION', ('HYPERTENSION')
    BLOOD_PRESSURE = 'BLOOD_PRESSURE', ('BLOOD PRESSURE')


class FormAssesmentStatus(models.TextChoices):

    ONGOING = 'ONGOING', ('ONGOING')
    COMPLETED = 'COMPLETED', ('COMPLETED')

   


# FormAssesment Model
class FormAssesment(models.Model):
    status = models.CharField(
        max_length=100,
        choices=FormAssesmentStatus.choices,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='form_assesments')
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='form_assesments', null=True, blank=True)
    
    prescription = models.OneToOneField(    
        Prescription, on_delete=models.CASCADE, related_name='form_assesments', null=True, blank=True)

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='form_assesments')
    
    subscription_form = models.OneToOneField(
        SubscriptionForm, on_delete=models.CASCADE, related_name='form_assesments', null=True, blank=True
    )


# SubscriptionForm Model
class SubscriptionForm(models.Model):

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    delivered_on = models.DateTimeField()
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='subscription_forms')
    

# TreatmentType Model
class TreatmentType(models.Model):
    treatment_option = models.CharField(
        max_length=100,
        choices=TreatmentOption.choices,)


# Question Model
class Question(models.Model):
    question = models.TextField()
    treatment_type = models.ManyToManyField(
        TreatmentType,  related_name='questions')


# Answer Model
class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    form_assesment = models.ForeignKey(
        FormAssesment, on_delete=models.CASCADE, related_name='answers')


# Avalability Model
class Avalability(models.Model):
    
   date = models.DateField()
   start_time = models.TimeField()
   duration = models.IntervalField()
   doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='avalabilities')
    
    

# Appointment Model
class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='appointments')
    booked = models.BooleanField(default=False)
    availability = models.OneToOneField(
        Avalability, on_delete=models.CASCADE, related_name='appointment')

    prescription = models.OneToOneField(
        Prescription, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='appointments')

    

# Attachment Model
class Attachment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='attachments')
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='attachments')
    appointment = models.ForeignKey(
        Appointment, on_delete=models.CASCADE, related_name='attachments', null=True, blank=True)
