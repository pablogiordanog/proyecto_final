from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse 
# Create your views here.

def noticias(request):
    return render(request, 'noticias.html')

def registrar(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form':UserCreationForm})
    else:
     if request.POST['password1'] == request.POST['pasword2']:
         user = user.objects.createuser(username=request.POST['username'], password = request.POST ['password1'])
         user.save
         return HttpResponse('El usuario se creo bien')
     return HttpResponse('La contraseña no coincide')