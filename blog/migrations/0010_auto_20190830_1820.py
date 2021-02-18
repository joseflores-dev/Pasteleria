# Generated by Django 2.2.2 on 2019-08-30 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190830_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precioVenta',
            field=models.IntegerField(default='1', null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('NORMAL', 'normal'), ('VIP', 'vip')], default='NORMAL', max_length=15),
        ),
    ]