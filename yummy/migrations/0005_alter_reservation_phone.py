# Generated by Django 4.2.7 on 2023-12-06 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummy', '0004_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number should be in format: +380xxxxxxxxx', regex='^+?\\d{7,12}$')]),
        ),
    ]
