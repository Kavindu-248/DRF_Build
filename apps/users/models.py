from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

import uuid

from safedelete.models import SafeDeleteModel

from apps.common.email_templates import EmailTemplates
from apps.common.services import generate_token, send_mail
from django.dispatch import receiver


class Roles(models.TextChoices):
    # User Roles

    PATIENT = 'PATIENT', _('PATIENT')
    DOCTOR = 'DOCTOR', _('DOCTOR')
    PHARMACY_USER = 'PHARMACY_USER', _('PHARMACY_USER')


# Gender Choice
class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'


class User(AbstractUser, SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.USER
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def is_patient(self):
        return self.role == Roles.PATIENT

    def is_doctor(self):
        return self.role == Roles.DOCTOR

    def is_pharmacy_user(self):
        return self.role == Roles.PHARMACY_USER

    def generate_email_verification_code(self):
        verification = self.email_verifications.create(code=generate_token(6))
        send_mail(
            'Please confirm your email.',
            self.email,
            EmailTemplates.AUTH_VERIFICATION,
            {'verification_code': verification.code}
        )


class UserEmailVerification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='email_verifications'
    )
    code = models.PositiveIntegerField(max_length=6)
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


# Doctor Model
class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False)


# Patient Model
class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False)

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.MALE,
    )


# PharmacyUser
class PharmacyUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False)
