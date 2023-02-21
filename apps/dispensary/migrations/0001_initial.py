# Generated by Django 3.2.5 on 2023-02-21 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20230221_0827'),
        ('assesment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('pharmacy_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pharmacies', to='users.pharmacyuser')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('pharmacy', models.ManyToManyField(related_name='vaccines', to='dispensary.Pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('prescription_status', models.CharField(choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED')], default='PENDING', max_length=100)),
                ('verified', models.BooleanField(default=False)),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='assesment.appointment')),
                ('form_assesment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='assesment.formassesment')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED')], default='PENDING', max_length=100)),
                ('is_prepared', models.BooleanField(default=False)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='assesment.appointment')),
                ('form_assesment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='assesment.formassesment')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='dispensary.pharmacy')),
                ('prescription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='dispensary.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('pharmacy', models.ManyToManyField(related_name='medicines', to='dispensary.Pharmacy')),
                ('prescription', models.ManyToManyField(related_name='medicines', to='dispensary.Prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_provided', models.CharField(choices=[('FORM_ASSESMENTS_SERVICE', 'FORM ASSESMENTS SERVICE'), ('VIDEO_CONSULTATION', 'VIDEO CONSULTATION')], max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_option', models.CharField(choices=[('CREDIT_CARD', 'CREDIT CARD'), ('DEBIT_CARD', 'DEBIT CARD'), ('PAYPAL', 'PAYPAL')], max_length=100)),
                ('date_due', models.DateField()),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='dispensary.order')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vaccine', models.ManyToManyField(related_name='countries', to='dispensary.Vaccine')),
            ],
        ),
    ]
