from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

import uuid

from safedelete.models import SafeDeleteModel

from apps.common.email_templates import EmailTemplates
from apps.common.services import generate_token, send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class Roles(models.TextChoices):
    # User Roles
    SUPER_ADMIN = 'SUPER_ADMIN', _('SUPER_ADMIN')
    ADMIN = 'ADMIN', _('ADMIN')
    USER = 'USER', _('USER')
    PATIENT = 'PATIENT', _('PATIENT')
    DOCTOR = 'DOCTOR', _('DOCTOR')
    PHARMACY_USER = 'PHARMACY_USER', _('PHARMACY_USER')


base_role = Roles.USER


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

    def is_super_admin(self):
        return self.role == Roles.SUPER_ADMIN or self.is_superuser

    def is_admin_user(self):
        return self.role in [Roles.ADMIN, Roles.SUPER_ADMIN]

    def is_user(self):
        return self.role == Roles.USER

    def generate_email_verification_code(self):
        verification = self.email_verifications.create(code=generate_token(6))
        send_mail(
            'Please confirm your email.',
            self.email,
            EmailTemplates.AUTH_VERIFICATION,
            {'verification_code': verification.code}
        )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


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


# Doctor Manager
class DoctorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.role.DOCTOR)


class DoctorProfile(User):

    base_role = Roles.DOCTOR

    doctor = DoctorManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=DoctorProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "DOCTOR":
        DoctorProfile.objects.create(user=instance)


# Doctor Model
class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=True)


class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.role.PATIENT)


class PatientProfile(User):

    base_role = Roles.PATIENT

    patient = PatientManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=PatientProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "PATIENT":
        PatientProfile.objects.create(user=instance)


# Patient Model
class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=True)

    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.MALE,
    )


class PharmacyUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.role.PHARMACY_USER)


class PharmacyUserProfile(User):

    base_role = Roles.PHARMACY_USER

    pharmacy_user = PharmacyUserManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=PatientProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "PHARMACY_USER":
        PharmacyUserProfile.objects.create(user=instance)


# PharmacyUser
class PharmacyUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=True)
