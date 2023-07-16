from django.db import models

class Noticias(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    detalle = models.TextField()
    imagen = models.ImageField(upload_to='blog', default='blog/img.jpg')
    fecha_publicacion= models.DateTimeField(auto_now_add=True)
    
    def __srt__(self):
        return self.titulo
    
    
