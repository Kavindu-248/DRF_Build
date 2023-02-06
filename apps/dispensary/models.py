from django.db import models

from apps.users.models import PharmacyUser


# Pharamcy Model

class Pharmacy(models.Model):
    id = models(primary_key=True,  editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pharmacy_user = models.ForeignKey(
        PharmacyUser, on_delete=models.CASCADE, related_name='pharmacies', null=False)


# Prescription Model

class Prescription(models.Model):
    id = models(primary_key=True, editable=False)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Medicine Model

class Medicine(models.Model):
    id = models(primary_key=True,  editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    pharmacy = models.ManyToManyField(
        Pharmacy, related_name='medicines', null=False)


# Invoice Model

class Invoice(models.Model):
    id = models(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Order Model
class Order(models.Model):
    id = models(primary_key=True,  editable=False)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    pharmacy = models.ForeignKey(
        Pharmacy, on_delete=models.CASCADE, related_name='orders', null=True)


# Vaccine Model

class Vaccine(models.Model):
    id = models(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    pharmacies = models.ManyToManyField(
        Pharmacy, null=False, verbose_name='Pharmacies')


# Country Model
class Country(models.Model):
    id = models(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    vaccines = models.ManyToManyField(Vaccine, null=True)
