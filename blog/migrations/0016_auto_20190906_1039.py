# Generated by Django 2.2.3 on 2019-09-06 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190905_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cantidad',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]