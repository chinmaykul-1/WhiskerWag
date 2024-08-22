# Generated by Django 5.0.7 on 2024-08-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_doctor_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='pets_age',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pets_breed',
            field=models.CharField(default='Dont know', max_length=40),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pets_name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]