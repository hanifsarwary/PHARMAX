# Generated by Django 2.0.6 on 2018-12-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_supplier_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
