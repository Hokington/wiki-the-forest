from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse
#from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout


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
    datos = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmation = request.POST.get('confirmation')

        try:
            user = User.objects.get(email=email)
            datos['mensaje'] = "Ya hay un usuario con este correo."
            return render(request, 'proyecto1/registro.html', datos)
        except User.DoesNotExist:
            pass

        try:
            user = User.objects.get(nombre_usuario=name)
            datos['mensaje'] = "Ya hay un usuario con este nombre."
            return render(request, 'proyecto1/registro.html', datos)
        except User.DoesNotExist:
            pass
        
        if not password == confirmation:
            datos['mensaje'] = "Las contraseñas no coinciden."
            return render(request, 'proyecto1/registro.html', datos)
        
        User.objects.create(nombre_usuario=name, email=email, contrasena=password)
        datos['mensaje'] = "Usuario registrado exitosamente."
        return render(request, 'proyecto1/login.html', datos)
        
    return render(request, 'proyecto1/registro.html')

def login_view(request):
    datos = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email = email)

        except User.DoesNotExist:
            datos['mensaje'] = "No hay ningún usuario con este correo."
            return render(request, 'proyecto1/login.html', datos)

        if password == user.contrasena:
            request.session['user_id'] = user.id
            return redirect('mi-cuenta')
        else:
            datos['mensaje'] = "Contraseña incorrecta."
            return render(request, 'proyecto1/login.html', datos)

    return render(request, 'proyecto1/login.html', datos)

def recuperar(request):
    return render(request, 'proyecto1/recuperar.html')

def miCuenta(request):
    id = request.session.get('user_id')
    if id:
        user = User.objects.get(id = id)

        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            try:
                user.nombre_usuario = name
                user.email = email
                user.contrasena = password
                user.save()

            except:
                datos['mensaje'] = 'No se pudo actualizar los datos, revisa si están correctos.'
 
        datos = {
            'username':  user.nombre_usuario,
            'email': user.email,
            'password': user.contrasena,
            'imagen': user.imagen
        }
        
        return render(request, 'proyecto1/mi-cuenta.html', datos)
    else:
        return redirect('login')

def logout_view(request):
    request.session.clear()
    return redirect('index')