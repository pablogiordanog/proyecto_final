from django import forms
from .models import Usuario
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
    
