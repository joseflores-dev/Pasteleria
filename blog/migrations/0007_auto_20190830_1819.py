# Generated by Django 2.2.2 on 2019-08-30 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(max_length=15, null=True),
        ),
    ]
