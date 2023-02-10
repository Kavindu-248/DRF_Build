import datetime
from django.db import models

from apps.users.models import Patient, Doctor
from apps.files.models import File


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
        Doctor, on_delete=models.CASCADE, related_name='form_assesments', null=True)


# SubscriptionForm Model
class SubscriptionForm(models.Model):

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    delivered_on = models.DateTimeField()
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='subscription_forms')
    subscription_assesment = models.OneToOneField(
        FormAssesment, on_delete=models.CASCADE, related_name='subscription_form')


# TreatmentType Model
class TreatmentType(models.Model):
    treatment_option = models.CharField(
        max_length=100,
        choices=TreatmentOption.choices,)


# Question Model
class Question(models.Model):
    question = models.CharField(max_length=100)
    treatment_type = models.ManyToManyField(
        TreatmentType,  related_name='questions')


# Answer Model
class Answer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    FormAssesment = models.ForeignKey(
        FormAssesment, on_delete=models.CASCADE, related_name='answers')


# Avalability Model
class Avalability(models.Model):
    day = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='avalabilities')


# Appointment Model
class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='appointments')
    booked = models.BooleanField(default=False)
    attachment = models.ForeignKey(
        'Attachment', on_delete=models.CASCADE, related_name='appointments', null=True)
    avalability = models.OneToOneField(
        Avalability, on_delete=models.CASCADE, related_name='appointments')


# Attachment Model
class Attachment(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='attachments')
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='attachments')
    created_at = models.DateTimeField(auto_now_add=True)
