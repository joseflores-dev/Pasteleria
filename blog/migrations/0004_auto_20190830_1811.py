# Generated by Django 2.2.2 on 2019-08-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190830_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('NORMAL', 'normal'), ('VIP', 'vip')], default='RESCATADO', max_length=15),
        ),
    ]