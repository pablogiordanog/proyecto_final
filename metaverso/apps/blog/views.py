from django.shortcuts import render, redirect
##from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse 
# Create your views here.
from.models import Usuarios
from django.urls import reverse_lazy
from .forms import Usuarioform
from django.views.generic import CreateView


def noticias(request):
    return render(request, 'noticias.html')



"""def RegistrarUsuario(request):
    #if request.method == 'POST':
    form = Usuarioform(request.POST)
    if form.is_valid():
            form.save()
            #return redirect('inicio')
        
    else:
        form= Usuarioform()
    return render(request, 'registro.html', {'form': form})"""

class RegistrarUsuario(CreateView):
    model = Usuarios
    template_name = 'registro.html'
    form_class = Usuarioform
    success_url = reverse_lazy('inicio')




