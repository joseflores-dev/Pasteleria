from django import forms
from .models import Perfil,Producto,Reserva,Mensaje
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class perfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('descripcion',)


class reservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('cantidad',)

class CancelarReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('producto','usuario')
        widgets = {'producto': forms.HiddenInput(),'usuario':forms.HiddenInput()}

        

class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('titulo',)
        
class mensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('de','titulo','mensaje',)
        widgets= {'mensaje':forms.Textarea(attrs={'class':'textArea'})}
 

class registoUsuarioForm(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1", "password2",]
        widgets = {'username':forms.TextInput(attrs={'class':'input100','id':'input100'}),
                   'email':forms.TextInput(attrs={'class':'input100','id':'input100'}),
            'first_name':forms.TextInput(attrs={'class':'input100','id':'input100'}),
            'last_name':forms.TextInput(attrs={'class':'input100','id':'input100'}),
            'password1':forms.TextInput(attrs={'class':'input100','id':'input100'}),
            'password2':forms.TextInput(attrs={'class':'input100','id':'input100'})}

      


class filtrarForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria']
        widgets = {'categoria':forms.Select(attrs={'class':'filtro','id':'filtro'})}
        
