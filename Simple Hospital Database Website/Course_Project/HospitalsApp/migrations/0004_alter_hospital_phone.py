# Generated by Django 5.1.6 on 2025-03-30 20:20

import HospitalsApp.validate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalsApp', '0003_alter_hospital_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='phone',
            field=models.CharField(max_length=12, validators=[HospitalsApp.validate.validate_phone]),
        ),
    ]
