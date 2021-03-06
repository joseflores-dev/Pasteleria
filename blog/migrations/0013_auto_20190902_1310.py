# Generated by Django 2.2.3 on 2019-09-02 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/productos'),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('PEDIDO', 'pedido'), ('PROCESO', 'proceso'), ('FINALIZADO', 'finalizado')], default='NORMAL', max_length=15)),
                ('cantidad', models.IntegerField(default=0)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Producto')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
