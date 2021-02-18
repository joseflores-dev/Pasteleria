from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as log_in
from django.contrib.auth import logout as log_out
from django.contrib.auth.models import User
from .models import Producto,Perfil,Reserva,Mensaje
from .forms import reservaForm,productoForm,CancelarReservaForm,mensajeForm,registoUsuarioForm,loginUsuarioForm,filtrarForm
from django.utils import timezone
from django.db.models import Avg, Max, Min, Sum
from django.http import HttpResponse
from carton.cart import Cart
import sweetify
import json
# Create your views here.


def index(request):
    productos = Producto.objects.all()
    mensaje = mensajeForm()
    perfil = Perfil.objects.get(pk=1)
    if request.method == 'POST':
        mensaje = mensajeForm(request.POST)
        if mensaje.is_valid():
            mensaje.save()
            mensaje = mensajeForm()
            sweetify.success(request,'Mensaje correcto',text='Se ha enviado el mensaje con exito',button='Ok')
            return render(request,'index.html',{'productos':productos,'mensaje':mensaje,'perfil':perfil})
    else:
        if request.user.is_superuser:
            reservas = Reserva.objects.filter(estado="pedido").count()
            if reservas > 0:
                sweetify.success(request,'Reservas Pendientes',text='Tienes '+str(reservas)+' Pedido En Espera',button='Ok')
        return render(request,'index.html',{'productos':productos,'mensaje':mensaje,'perfil':perfil})

def login(request):
    if request.method == 'POST':
        FormularioUsuario = loginUsuarioForm(data=request.POST)
        if FormularioUsuario.is_valid():
            user = FormularioUsuario.get_user()
            log_in(request,user)
            return redirect('blog:home')
        else:
            sweetify.error(request,'Usuario/Contraseña Incorrecta',text='Haz Ingresado Bien Tus Datos?',button='Ok')
    else:
        FormularioUsuario = loginUsuarioForm()
    return render(request,'login.htm', {'FormularioUsuario':FormularioUsuario})

def signup(request):
    if request.method == 'POST':
      
        newFormularioUsuario = registoUsuarioForm(request.POST)
        if newFormularioUsuario.is_valid():
            newFormularioUsuario.save()
            sweetify.success(request,'Correcto',text='Se ha registrado con exito',button='Ok')
            return redirect('blog:login')
        else:
            sweetify.error(request,'Error',text='Siga el formato establecido',button='Ok')
            FormularioUsuario = registoUsuarioForm()
            return render(request,'registro.htm',{'Registro':FormularioUsuario})
    else:
        newFormularioUsuario = registoUsuarioForm()
    return render(request,'registro.htm',{'Registro':newFormularioUsuario})


def logout(request):
    if request.method == 'POST':
        log_out(request) 
        return redirect('blog:home')


def contacto(request):
    perfil = Perfil.objects.get(pk=1)
    mensaje = mensajeForm()
    if request.method == "POST":
        mensaje = mensajeForm(request.POST)
        if mensaje.is_valid():
            mensaje.save()
            mensaje = mensajeForm()
            sweetify.success(request,'Correcto',text='Mensaje Enviado Con Exito',button='Ok')
            return render(request,'contact.html',{'perfil':perfil,'mensaje':mensaje})
    return render(request,'contact.html',{'perfil':perfil,'mensaje':mensaje})



def verProducto(request,pk):
    
    seleccionado = Producto.objects.get(pk=pk)
    relacionados = Producto.objects.filter(categoria=seleccionado.categoria)
    reserva = reservaForm()
    todasReservas = Reserva.objects.filter(usuario=request.user,producto=seleccionado,estado = "pedido")
    try:
        verificarReserva = Reserva.objects.get(usuario = request.user, producto=seleccionado,estado = 'pedido')
        formularioCancelar = CancelarReservaForm(instance=verificarReserva)
    except Reserva.DoesNotExist:
        verificarReserva = None
        formularioCancelar = CancelarReservaForm()
    
    if request.method == "POST":
        reserva = reservaForm(request.POST)
        formularioCancelar = CancelarReservaForm(request.POST)
        if reserva.is_valid():
            reserva = reserva.save(commit=False)
            reserva.total = reserva.cantidad*seleccionado.precioVenta
            reserva.usuario = request.user
            reserva.producto = seleccionado
            reserva.fecha_publicacion = timezone.now()
            cart = Cart(request.session)
            cart.add(seleccionado, price=seleccionado.precio)
            if verificarReserva == None:
                reserva.save()
                verificarReserva = Reserva.objects.get(usuario = request.user,producto=seleccionado,estado="pedido")
                sweetify.success(request,'Correcto',text='Su reserva se ha terminado correctamente',button='Ok')
                if verificarReserva != None:
                    formularioCancelar = CancelarReservaForm(instance=verificarReserva)
                return render(request,'verProducto.htm',{'producto':seleccionado,'verificarReserva':verificarReserva,'formularioCancelar':formularioCancelar,'relacionados':relacionados})         
            else:
                sweetify.error(request,'Error',text='Su pedido se encuentra en proceso',button='Ok')
                return render(request,'verProducto.htm',{'producto':seleccionado,'verificarReserva':verificarReserva,'formularioCancelar':formularioCancelar,'relacionados':relacionados})
        elif formularioCancelar.is_valid():
                instance = Reserva.objects.get(producto=seleccionado,usuario=request.user,pk=verificarReserva.id)
                instance.delete()
                sweetify.success(request,'success',text='Su pedido a sido cancelado con exito',button='Ok')
                return render(request,'verProducto.htm',{'producto':seleccionado,'reserva':reserva,'relacionados':relacionados})   
    else:
        if verificarReserva != None:
            formularioCancelar = CancelarReservaForm(instance=verificarReserva)
        return render(request,'verProducto.htm',{'producto':seleccionado,'reserva':reserva,'verificarReserva':verificarReserva,'formularioCancelar':formularioCancelar,'relacionados':relacionados})
    
    
def verTodos(request):
    filtro = filtrarForm()
    if request.method == "POST":
        filtro = filtrarForm(request.POST)
        if filtro.is_valid():
            categoria = request.POST['categoria']
            productos = Producto.objects.filter(categoria=categoria)
            filtro = filtrarForm()
            return render(request,'verTodos.html',{'filtro':filtro,'productos':productos})
    productos = Producto.objects.all()
    return render(request,'verTodos.html',{'productos':productos,'filtro':filtro})

def verPedidos(request):
    pedidos = Reserva.objects.filter(usuario=request.user)
    for misPedidos in pedidos:
        producto = Producto.objects.filter(id=misPedidos.producto_id)
    return render(request,'verPedidos.html',{'pedidos':pedidos,'producto':producto})

def eliminarPedido(request,pk):
    instance = Reserva.objects.get(pk=pk)
    instance.delete()
    sweetify.success(request,'success',text='Su pedido a sido cancelado con exito',button='Ok')
    pedidos = Reserva.objects.filter(usuario=request.user)
    for misPedidos in pedidos:
        producto = Producto.objects.filter(id=misPedidos.producto.id)
    return render(request,'verPedidos.html',{'pedidos':pedidos,'producto':producto})

def estadisticas(request):
    estadisticas = Reserva.objects.all().values('producto__titulo').order_by('producto').annotate(cantidad=Sum('cantidad'),total=Sum('total'),fecha_publicacion=Max('fecha_publicacion'))
    return render(request,'estadisticas.html',{'estadisticas':estadisticas})



def eliminarPedidoAjax(request):
    if request.method == 'POST':
        if request.is_ajax():
            data = request.POST['mydata']
            instance = Reserva.objects.get(pk=data)
            if instance.estado == "pedido":   
                instance.delete()
                pedidos = Reserva.objects.filter(usuario=request.user)
                for misPedidos in pedidos:
                    producto = Producto.objects.filter(id=misPedidos.producto.id)
    return render(request,'verPedidos.html',{'pedidos':pedidos,'producto':producto})

            
    