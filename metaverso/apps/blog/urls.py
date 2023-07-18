from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views 
from .views import RegistrarUsuario



urlpatterns = [
    path('noticias/', views.noticias, name='noticias'),
    path('registro/', RegistrarUsuario.as_view(), name='registro')
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)