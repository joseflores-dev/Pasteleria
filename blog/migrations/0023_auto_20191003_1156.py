# Generated by Django 2.2.2 on 2019-10-03 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='descripcion2',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='titulo2',
        ),
    ]
