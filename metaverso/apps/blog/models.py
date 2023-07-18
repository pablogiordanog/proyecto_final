from django.db import models
from django.contrib.auth.models import AbstractUser

class Noticias(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    detalle = models.TextField()
    imagen = models.ImageField(upload_to='blog', default='blog/img.jpg')
    fecha_publicacion= models.DateTimeField(auto_now_add=True)
    
    def __srt__(self):
        return self.titulo
    
class Usuarios(AbstractUser):  
    nombre = models.CharField(max_length=20, null=True) 
    apellido = models.CharField(max_length=20, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    es_colaborador = models.BooleanField('es_colaborador', default=False)
    imagen = models.ImageField(upload_to='blog')
    email = models.EmailField(null=True, blank=True)

    
    
    #def __srt__(self):
        #return self.nombre
    

