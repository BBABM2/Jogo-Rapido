from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import QuadraGeral

def inicio(request):
 return render(request, 'inicio.html')
  
def login_usuario(request):
 formulario = AuthenticationForm()
 if request.method == 'POST' and request.POST:
    formulario = AuthenticationForm(request, request.POST)
    if formulario.is_valid(): # se usuário e senha estão corretos
        usuario = formulario.get_user()
        login(request, usuario)
        return redirect('/home')
    return render(request, 'login.html', {'formulario': formulario})



def home(request):
    quadrasgeral = QuadraGeral.objects.all()
    return render(request, 'home.html', context= {'quadrasgeral': quadrasgeral})
        

def logout_usuario(request):
 logout(request)
 return redirect('/')
