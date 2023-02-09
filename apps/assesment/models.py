import datetime
from django.db import models

from apps.users.models import Patient, Doctor
from apps.files.models import File

# Choice Fields


class TreatmentOptions(models.TextChoices):

    DIABETES = 'DIABETES', ('DIABETES')
    CHOLESTREROL = 'CHOLESTREROL', ('CHOLESTREROL')
    HYPERTENSION = 'HYPERTENSION', ('HYPERTENSION')
    BLOOD_PRESSURE = 'BLOOD_PRESSURE', ('BLOOD PRESSURE')


class Status(models.TextChoices):

    ONGOING = 'ONGOING', ('ONGOING')
    COMPLETED = 'COMPLETED', ('COMPLETED')


# FormAssesment Model
class FormAssesment(models.Model):
    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.ONGOING
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


# TreatmentType Model
class TreatmentType(models.Model):
    treatment_options = models.CharField(
        max_length=100,
        choices=TreatmentOptions.choices,
        default=TreatmentOptions.DIABETES)


# Question Model
class Question(models.Model):
    question = models.CharField(max_length=100)
    answered = models.BooleanField(default=False)
    treatment_types = models.ManyToManyField(
        TreatmentType,  related_name='questions')


# Answer Model
class Answer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    FormAssesment = models.ForeignKey(
        FormAssesment, on_delete=models.CASCADE, related_name='answers')


# Appointment Model
class Appointment(models.Model):

    date = models.DateTimeField()
    time = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='appointments')


# Avalability Model
class Consultation(models.Model):
    day = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    slot_duration = models.DurationField(
        default=datetime.timedelta(minutes=15))
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='avalabilities', null=True)


# Attachment Model
class Attachment(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='attachments')
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='attachments')
    created_at = models.DateTimeField(auto_now_add=True)
