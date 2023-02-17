# Generated by Django 3.2.5 on 2023-02-17 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('files', '0001_initial'),
        ('assesment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionform',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_forms', to='users.patient'),
        ),
        migrations.AddField(
            model_name='question',
            name='treatment_type',
            field=models.ManyToManyField(related_name='questions', to='assesment.TreatmentType'),
        ),
        migrations.AddField(
            model_name='formassesment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form_assesments', to='users.doctor'),
        ),
        migrations.AddField(
            model_name='formassesment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_assesments', to='users.patient'),
        ),
        migrations.AddField(
            model_name='avalability',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avalabilities', to='users.doctor'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='assesment.appointment'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='files.file'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='users.patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='availability',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='assesment.avalability'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='users.patient'),
        ),
        migrations.AddField(
            model_name='answer',
            name='form_assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='assesment.formassesment'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='assesment.question'),
        ),
    ]
