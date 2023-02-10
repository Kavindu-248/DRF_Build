from django.db import models
from apps.users.models import PharmacyUser


# Choice Fields

class OrderStatus(models.TextChoices):
    PENDING = 'PENDING', ('PENDING')
    ACCEPTED = 'ACCEPTED', ('ACCEPTED')
    REJECTED = 'REJECTED', ('REJECTED')


class ServiceProvided(models.TextChoices):
    FORM_ASSESMENTS_SERVICE = 'FORM_ASSESMENTS_SERVICE', (
        'FORM ASSESMENTS SERVICE')
    VIDEO_CONSULTATION = 'VIDEO_CONSULTATION', ('VIDEO CONSULTATION')


class PaymentOptions(models.TextChoices):
    CREDIT_CARD = 'CREDIT_CARD', ('CREDIT CARD')
    DEBIT_CARD = 'DEBIT_CARD', ('DEBIT CARD')
    PAYPAL = 'PAYPAL', ('PAYPAL')


class PrescriptionStatus(models.TextChoices):
    PENDING = 'PENDING', ('PENDING')
    ACCEPTED = 'ACCEPTED', ('ACCEPTED')
    REJECTED = 'REJECTED', ('REJECTED')


# Pharamcy Model
class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    pharmacy_user = models.ForeignKey(
        PharmacyUser, on_delete=models.CASCADE, related_name='pharmacies')


# Prescription Model

class Prescription(models.Model):
    medication = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    prescription_status = models.CharField(
        max_length=100,
        choices=PrescriptionStatus.choices,
        default=PrescriptionStatus.PENDING


    )

    verified = models.BooleanField(default=False)


# Medicine Model
class Medicine(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    pharmacy = models.ManyToManyField(
        Pharmacy, related_name='medicines', related_name='Pharmacies')


# Invoice Model

class Invoice(models.Model):
    service_provided = models.CharField(
        max_length=100,
        choices=ServiceProvided.choices,
    )

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_option = models.CharField(
        max_length=100,
        choices=PaymentOptions.choices,
    )

    date_due = models.DateField()

# Order Model


class Order(models.Model):
    order_status = models.CharField(
        max_length=100,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING

    )
    pharmacy = models.ForeignKey(
        Pharmacy, on_delete=models.CASCADE, related_name='orders')

# Vaccine Model


class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    pharmacy = models.ManyToManyField(
        Pharmacy,  related_name='Pharmacies')


# Country Model
class Country(models.Model):
    name = models.CharField(max_length=100)
    vaccine = models.ManyToManyField(
        Vaccine, null=True, related_name='Vaccines', null=True)
