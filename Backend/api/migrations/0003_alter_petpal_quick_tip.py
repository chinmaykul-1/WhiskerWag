# Generated by Django 5.0.7 on 2024-08-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_petpal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petpal',
            name='Quick_tip',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
