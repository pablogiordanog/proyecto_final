from django.db import models
from django.contrib.auth.models import AbstractUser

class Noticia(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    detalle = models.TextField()
    imagen = models.ImageField(upload_to='blog', default='blog/img.jpg')
    fecha_publicacion= models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey("Categoria", on_delete = models.SET_NULL,null=True)
    def __srt__(self):
        return self.titulo

class Usuario(AbstractUser):  
    nombre = models.CharField(max_length=20, null=True) 
    apellido = models.CharField(max_length=20, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    es_colaborador = models.BooleanField('es_colaborador', default=False)
    imagen = models.ImageField(upload_to='blog')
    email = models.EmailField(null=True, blank=True)
    #def __srt__(self):
        #return self.nombre

class Categoria(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    coticia=models.ForeignKey(Noticia, on_delete = models.CASCADE)
    usuario=models.ForeignKey(Usuario, on_delete = models.SET_NULL, null=True)
    texto = models.TextField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

