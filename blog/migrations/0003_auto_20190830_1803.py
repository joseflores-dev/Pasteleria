# Generated by Django 2.2.2 on 2019-08-30 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_productos_tipo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]