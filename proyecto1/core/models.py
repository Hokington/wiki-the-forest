from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id usuario',)
    imagen = models.CharField(max_length=50, default='', verbose_name='Ruta de imagen')
    email = models.EmailField(max_length=50, verbose_name='Correo Electrónico', unique=True)
    nombre_usuario = models.CharField(max_length=100, verbose_name='Nombre de Usuario', unique=True)
    es_admin = models.BooleanField(default=False, verbose_name='Es administrador')
    contrasena = models.CharField(max_length=100, verbose_name='Contraseña')

    def str(self):
        return self.nombre_usuario