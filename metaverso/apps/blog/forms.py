from django import forms
from .models import Usuario,Noticia,Comentario,Categoria
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class Usuarioform(UserCreationForm):
    class Meta:
        model = Usuario
        fields= [ 
            
            'nombre',
            'apellido',
            'username',
            'email',
            'fecha_nacimiento',
            'password1',
            'password2',
            'imagen',      
        ]
        
        
    @transaction.atomic
    def save(self):
        user              = super().save(commit=False)
        user.is_superuser = False
        user.is_staff     = False
        user.save()
        return user
    

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ("titulo", "detalle", "imagen","categoria")
    def __init__(self, *args, **kwargs):
        super(NoticiaForm, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs.update({'placeholder' : 'titulo del post', 'type' : 'text'})
        self.fields["detalle"].widget.attrs.update({'placeholder' : 'Escriba su Noticia:', 'type' : 'text'})
        self.fields["imagen"].widget.attrs.update({'placeholder' : '', 'type' : 'file'})
        self.fields["categoria"].widget.attrs.update({'placeholder' : 'Ingrese Categoria', 'type' : ''})

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields =("texto",)
    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields["texto"].widget.attrs.update({'class' : 'materialize-textarea','placeholder' : 'Escriba su comentario', 'type' : 'text'})

#se puede cargar por bd y no se hace la vista para admin
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ("titulo","descripcion")