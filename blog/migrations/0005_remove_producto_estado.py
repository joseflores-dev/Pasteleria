# Generated by Django 2.2.2 on 2019-08-30 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190830_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='estado',
        ),
    ]
