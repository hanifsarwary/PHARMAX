# Generated by Django 2.1.4 on 2018-12-06 16:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_auto_20181206_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_username', message='name must be alphabets', regex='^[A-Z][a-z]*$')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='phone number must be numeric', regex='^[0-9]*$')]),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='manu_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_username', message='name must be alphabets', regex='^[A-Z][a-z]*$')]),
        ),
    ]
