# Generated by Django 4.0 on 2021-12-21 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dental_clinic', '0005_remove_oficce_contact_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='message',
        ),
        migrations.RemoveField(
            model_name='users',
            name='subject',
        ),
        migrations.AddField(
            model_name='users',
            name='appointment_day',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='appointment_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='doctors',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dental_clinic.doctors'),
        ),
        migrations.AddField(
            model_name='users',
            name='service',
            field=models.ForeignKey(blank=True, max_length=150, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dental_clinic.service'),
        ),
    ]
