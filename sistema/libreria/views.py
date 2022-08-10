import re
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Valija
from .forms import ValijaForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def valijas(request):
    valijas = Valija.objects.all()
    return render(request, 'libros/index.html',{'valijas': valijas})

def crear(request):
    formulario = ValijaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('valijas')
    return render(request, 'libros/crear.html', {'formulario' : formulario })

def editar(request):
    return render(request, 'libros/editar.html')


def eliminar(request, id):
    valija = Valija.objects.get(id=id)
    valija.delete()
    return redirect('valijas')

def editar(request, id):
    valija = Valija.objects.get(id=id)
    formulario = ValijaForm(request.POST or None, request.FILES or None, instance=valija)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('valijas')
    return render(request, 'libros/editar.html', {'formulario' : formulario })
