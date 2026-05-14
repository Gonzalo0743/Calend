from rest_framework import serializers
from .models import Bot, Cita, Contacto


class BotSerializer(serializers.ModelSerializer):
    conversaciones = serializers.SerializerMethodField()

    class Meta:
        model = Bot
        fields = ['id', 'nombre', 'cliente', 'estado', 'flujo', 'conversaciones', 'creado', 'modificado']

    def get_conversaciones(self, obj):
        return obj.cita_set.count()


class CitaSerializer(serializers.ModelSerializer):
    iniciales = serializers.SerializerMethodField()

    class Meta:
        model = Cita
        fields = ['id', 'nombre', 'servicio', 'hora', 'estado', 'bot', 'iniciales', 'creado']

    def get_iniciales(self, obj):
        partes = obj.nombre.strip().split()
        if len(partes) >= 2:
            return partes[0][0].upper() + partes[1][0].upper()
        return partes[0][0].upper()


class ContactoSerializer(serializers.ModelSerializer):
    iniciales = serializers.SerializerMethodField()
    ultima_interaccion = serializers.SerializerMethodField()
    citas = serializers.SerializerMethodField()
    bot_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Contacto
        fields = ['id', 'nombre', 'telefono', 'canal', 'bot', 'bot_nombre', 'iniciales', 'ultima_interaccion', 'citas', 'creado']

    def get_iniciales(self, obj):
        partes = obj.nombre.strip().split()
        if len(partes) >= 2:
            return partes[0][0].upper() + partes[1][0].upper()
        return partes[0][0].upper()

    def get_ultima_interaccion(self, obj):
        from django.utils.timesince import timesince
        return f'Hace {timesince(obj.ultima_interaccion)}'

    def get_citas(self, obj):
        return Cita.objects.filter(nombre=obj.nombre).count()

    def get_bot_nombre(self, obj):
        return obj.bot.nombre if obj.bot else ''