from django.conf.urls import include, url
from . import views

app_name='blog' 


urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'login$',views.login,name='login'),
    url(r'signup$',views.signup,name="signup"),
    url(r'logout$',views.logout,name="logout"),
    url(r'contacto$',views.contacto,name="contacto"),
    url(r'verProducto/(?P<pk>[0-9]+)/$',views.verProducto,name='verProducto'),
    url(r'verTodos/$',views.verTodos,name='verTodos'),
    url(r'misPedidos/$',views.verPedidos,name='verPedidos'),
    url(r'estadisticas/$',views.estadisticas,name='estadisticas'),
    url(r'eliminarPedido/ProductoSeleccionado/(?P<pk>[0-9]+)/$',views.eliminarPedido,name='eliminarPedido'),
    url(r'ajax/BorrarReserva/$',views.eliminarPedidoAjax,name='eliminarPedidoAjax'),
    
   
]
