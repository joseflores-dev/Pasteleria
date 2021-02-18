from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Categoria(models.Model):
    tipo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.fecha_creacion = timezone.now()
        self.save()
    
    def __str__(self):
        return self.tipo

class Producto(models.Model):
    foto = models.ImageField(blank=True,null=True,upload_to="media/productos")
    descripcion = models.CharField(max_length=900)
    titulo = models.CharField(max_length=30)
    tipo_choices = (
                     ('NORMAL','normal'),
                     ('VIP','vip'),
                     
    )
    tipo = models.CharField(max_length=15,choices=tipo_choices,default='NORMAL')
    precioVenta = models.IntegerField(null=True,default=0)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL, null=True)
    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()
        
    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto,on_delete=models.SET_NULL, null=True)
    tipo_choices = (
                     ('PEDIDO','pedido'),
                     ('PROCESO','proceso'),
                     ('FINALIZADO','finalizado'),
                     
    )
    estado = models.CharField(max_length=15,choices=tipo_choices,default='pedido')
    cantidad = models.IntegerField(null=False,default=0,validators=[MinValueValidator(1), MaxValueValidator(100)])
    total = models.IntegerField(null=False,default=0)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()
        
    def __str__(self):
        return 'Estado : '+self.estado+'  | Pedido Por : '+ self.usuario.username



class Perfil(models.Model):
    foto = models.ImageField(blank=True,null=True,upload_to="images/")
    descripcion = models.CharField(max_length=900)
    titulo1 = models.CharField(max_length=900)
    descripcion1 = models.CharField(max_length=900)
   

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()
        
    def __str__(self):
        return self.titulo1
    
class Mensaje(models.Model):
    de = models.CharField(max_length=900,default="")
    titulo = models.CharField(max_length=900)
    mensaje = models.CharField(max_length=900)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()
        
    def __str__(self):
        return self.de+': '+self.titulo



