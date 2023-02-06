from django.db import models
from apps.users.models import Patient, Doctor
from apps.files.models import File


# FormAssesment Model
class FormAssesment(models.Model):
    form_assesment_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='form_assesments', null=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='form_assesments', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# SubscriptionForm Model
class SubscriptionForm(models.Model):
    subscription_form_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='subscription_forms', null=True)


# TreatmentType Model
class TreatmentType(models.Model):
    treatment_type_id = models.IntegerField(primary_key=True)
    sickness_type = models.CharField(max_length=100)


# Question Model
class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=100)
    treatment_types = models.ManyToManyField(
        TreatmentType, null=False, related_name='questions')


# Answer Model
class Answer(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers', null=True)
    formAssesment = models.ForeignKey(
        FormAssesment, on_delete=models.CASCADE, related_name='answers', null=False)


# Avalability Model

class Avalability(models.Model):
    avalanility_id = models.IntegerField(primary_key=True)
    day = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='avalabilities', null=True)


# Appointment Model
class Appointment(models.Model):
    appointment_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='appointments', null=True)


# Attachment Model
class Attachment(models.Model):
    attachment_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='attachments', null=True,)
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='attachments')
    created_at = models.DateTimeField(auto_now_add=True)
