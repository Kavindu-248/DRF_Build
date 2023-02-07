from django.db import models
from apps.users.models import Patient, Doctor
from apps.files.models import File


# FormAssesment Model
class FormAssesment(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='form_assesments', null=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='form_assesments', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# SubscriptionForm Model
class SubscriptionForm(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='subscription_forms', null=True)


# TreatmentType Model
class TreatmentType(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    sickness_type = models.CharField(max_length=100)


# Question Model
class Question(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    text = models.CharField(max_length=100)
    treatment_types = models.ManyToManyField(
        TreatmentType, null=False, related_name='questions')


# Answer Model
class Answer(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    text = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers', null=True)
    FormAssesment = models.ForeignKey(
        FormAssesment, on_delete=models.CASCADE, related_name='answers', null=False)


# Avalability Model

class Avalability(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    day = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='avalabilities', null=True)


# Appointment Model
class Appointment(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    status = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='appointments', null=True)


# Attachment Model
class Attachment(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='attachments', null=True,)
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='attachments')
    created_at = models.DateTimeField(auto_now_add=True)
