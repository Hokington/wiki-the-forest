from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, 'proyecto1/index.html')

def categoria(request, categoria_nombre):

    template_path = f'proyecto1/categorias/{categoria_nombre}.html'
    
    get_template(template_path)
    context = {
        'categoria': categoria_nombre
    }
    return render(request, template_path, context)

def foro(request):
    return render(request, 'proyecto1/foro.html')

def registro(request):
    return render(request, 'proyecto1/registro.html')

def login(request):
    return render(request, 'proyecto1/login.html')

def recuperar(request):
    return render(request, 'proyecto1/recuperar.html')

def miCuenta(request):
    return render(request, 'proyecto1/mi-cuenta.html')
