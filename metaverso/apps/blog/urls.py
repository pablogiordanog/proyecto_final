from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('noticias/', views.noticias, name='noticias'),
    path('registro/', views.registrar, name= 'registro')
    
    
]