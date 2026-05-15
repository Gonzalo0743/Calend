from django.db import models
from django.contrib.auth.models import User


class Bot(models.Model):
    nombre = models.CharField(max_length=200)
    cliente = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, default='Borrador')
    flujo = models.JSONField(default=dict, blank=True)
    usuario = models.OneToOneField(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bot'
    )
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    ESTADOS = [
        ('Confirmada', 'Confirmada'),
        ('Pendiente', 'Pendiente'),
        ('Cancelada', 'Cancelada'),
    ]

    nombre = models.CharField(max_length=200)
    servicio = models.CharField(max_length=200)
    hora = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='Pendiente')
    bot = models.ForeignKey(Bot, on_delete=models.SET_NULL, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} - {self.hora}'


class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50, blank=True)
    canal = models.CharField(max_length=100)
    bot = models.ForeignKey(Bot, on_delete=models.SET_NULL, null=True, blank=True)
    ultima_interaccion = models.DateTimeField(auto_now=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre