import datetime
from django.db import models
from django.forms import ValidationError
from apps.users.models import Patient, Doctor
from apps.files.models import File


class Sickness(models.TextChoices):

    DIABETES = 'DIABETES', 'Diabetes'
    CHOLESTREROL = 'CHOLESTREROL', 'Cholestrerol'
    HYPERTENSION = 'HYPERTENSION', 'Hypertension'
    BLOOD_PRESSURE = 'BLOOD_PRESSURE', 'Blood Pressure'


# FormAssesment Model
class FormAssesment(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='ongoing'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='form_assesments', null=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='form_assesments', null=True)


# SubscriptionForm Model
class SubscriptionForm(models.Model):
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='subscription_forms', null=True)


# TreatmentType Model

class TreatmentType(models.Model):
    sickness = models.CharField(
        max_length=100,
        choices=Sickness.choices,
        default=Sickness.DIABETES)


# Question Model
class Question(models.Model):
    text = models.CharField(max_length=100)
    treatment_types = models.ManyToManyField(
        TreatmentType, null=False, related_name='questions')


# Answer Model
class Answer(models.Model):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers', null=True)
    FormAssesment = models.ForeignKey(
        FormAssesment, on_delete=models.CASCADE, related_name='answers', null=False)


# Avalability Model
class Avalability(models.Model):
    day = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    slot_duration = models.DurationField(
        default=datetime.timedelta(minutes=15))
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='avalabilities', null=True)


# Appointment Model
class Appointment(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='appointments', null=True)


# Attachment Model
class Attachment(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='attachments', null=True,)
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='attachments')
    created_at = models.DateTimeField(auto_now_add=True)
