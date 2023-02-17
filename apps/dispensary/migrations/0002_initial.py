# Generated by Django 3.2.5 on 2023-02-17 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('assesment', '0001_initial'),
        ('dispensary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='pharmacy_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacies', to='users.pharmacyuser'),
        ),
        migrations.AddField(
            model_name='order',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='assesment.appointment'),
        ),
        migrations.AddField(
            model_name='order',
            name='form_assesment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='assesment.formassesment'),
        ),
        migrations.AddField(
            model_name='order',
            name='pharmacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='dispensary.pharmacy'),
        ),
        migrations.AddField(
            model_name='order',
            name='prescription',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='dispensary.prescription'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='pharmacy',
            field=models.ManyToManyField(related_name='medicines', to='dispensary.Pharmacy'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='prescription',
            field=models.ManyToManyField(related_name='medicines', to='dispensary.Prescription'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='dispensary.order'),
        ),
        migrations.AddField(
            model_name='country',
            name='vaccine',
            field=models.ManyToManyField(related_name='countries', to='dispensary.Vaccine'),
        ),
    ]
