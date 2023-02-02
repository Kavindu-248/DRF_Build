from django.db import models
import uuid

from apps.users.models import Patient, Doctor


# FormAssesment Model

class FormAssesment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='form_assesments')
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='form_assesments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# SubscriptionForm Model
class SubscriptionForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='subscription_forms')

    def __str__(self):
        return self.description


# TreatmentType Model
class TreatmentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sickness_type = models.CharField(max_length=100)

    def __str__(self):
        return self.sickness_type


# Question Model
class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=100)
    treatment_types = models.ManyToManyField(TreatmentType)

    def __str__(self):
        return self.text


# Answer Model
class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    formAssesment = models.ForeignKey(
        FormAssesment, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text


# Avalability Model

class Avalability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='avalabilities')

    def __str__(self):
        return self.day


# Appointment Model

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='appointments')

    def __str__(self):
        return self.date
