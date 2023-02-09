from django.db import models
from apps.users.models import PharmacyUser


# Pharamcy Model

class Pharmacy(models.Model):

    class OrderStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        REJECTED = 'REJECTED', 'Rejected'

    order_status = models.CharField(
        max_length=100,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    pharmacy_user = models.ForeignKey(
        PharmacyUser, on_delete=models.CASCADE, related_name='pharmacies', null=False)


# Prescription Model

class Prescription(models.Model):
    medication = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)


# Medicine Model
class Medicine(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    pharmacy = models.ManyToManyField(
        Pharmacy, related_name='medicines', null=False, related_name='Pharmacies')


# Invoice Model

class Invoice(models.Model):

    date_created = models.DateField(auto_now_add=True)
    SERVICE_PROVIDED = [
        ('FORM_ASSESMENTS', 'Form Assesments'),
        ('VIDEO_CONSILTATION', 'Video Consultation'),
    ]
    service_provided = models.CharField(
        max_length=100,
        choices=SERVICE_PROVIDED,
        default='FORM_ASSESMENTS'
    )

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    PAYMENT_OPTIONS = [
        ('CREDIT_CARD', 'Credit Card'),
        ('DEBIT_CARD', 'Debit Card'),
        ('PAYPAL', 'Paypal'),
    ]
    payment_option = models.CharField(
        max_length=100,
        choices=PAYMENT_OPTIONS,
        default='CREDIT_CARD'
    )

    date_due = models.DateField()


# Order Model
# #class Order(models.Model):
#     accepted = models.BooleanField(default=False)
#     rejected = models.BooleanField(default=False)
#     pharmacy = models.ForeignKey(
#        Pharmacy, on_delete=models.CASCADE, related_name='orders', null=True)

# Vaccine Model
class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    pharmacies = models.ManyToManyField(
        Pharmacy, null=False, related_name='Pharmacies')


# Country Model
class Country(models.Model):
    name = models.CharField(max_length=100)
    vaccines = models.ManyToManyField(
        Vaccine, null=True, related_name='Vaccines')
