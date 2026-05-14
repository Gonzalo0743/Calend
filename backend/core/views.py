from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Bot, Cita, Contacto
from .serializers import BotSerializer, CitaSerializer, ContactoSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    identifier = request.data.get('username')
    password = request.data.get('password')

    if not identifier or not password:
        return Response(
            {'error': 'Por favor ingresa usuario y contraseña'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = None
    if '@' in identifier:
        try:
            db_user = User.objects.get(email=identifier)
            user = authenticate(request, username=db_user.username, password=password)
        except User.DoesNotExist:
            pass
    else:
        user = authenticate(request, username=identifier, password=password)

    if user is None:
        return Response(
            {'error': 'Credenciales incorrectas'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    tokens = get_tokens_for_user(user)

    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_staff': user.is_staff,
        'role': 'admin' if user.is_staff else 'client',
        'access': tokens['access'],
        'refresh': tokens['refresh'],
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    return Response({'message': 'Sesion cerrada correctamente'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_staff': user.is_staff,
        'role': 'admin' if user.is_staff else 'client',
    })


# --- Bots ---

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def bots_list(request):
    if request.method == 'GET':
        bots = Bot.objects.all().order_by('-modificado')
        serializer = BotSerializer(bots, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def bot_detail(request, pk):
    try:
        bot = Bot.objects.get(pk=pk)
    except Bot.DoesNotExist:
        return Response({'error': 'Bot no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BotSerializer(bot)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BotSerializer(bot, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Citas ---

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def citas_list(request):
    if request.method == 'GET':
        citas = Cita.objects.all().order_by('hora')
        serializer = CitaSerializer(citas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def cita_detail(request, pk):
    try:
        cita = Cita.objects.get(pk=pk)
    except Cita.DoesNotExist:
        return Response({'error': 'Cita no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = CitaSerializer(cita, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Contactos ---

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def contactos_list(request):
    if request.method == 'GET':
        contactos = Contacto.objects.all().order_by('-ultima_interaccion')
        serializer = ContactoSerializer(contactos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Metricas ---

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def metricas(request):
    from django.utils import timezone
    from datetime import timedelta

    hoy = timezone.now().date()
    inicio_semana = hoy - timedelta(days=7)

    return Response({
        'bots_activos': Bot.objects.filter(estado='Activo').count(),
        'citas_hoy': Cita.objects.filter(creado__date=hoy).count(),
        'citas_mes': Cita.objects.filter(creado__month=hoy.month).count(),
        'contactos': Contacto.objects.count(),
        'conversaciones_semana': Cita.objects.filter(creado__date__gte=inicio_semana).count(),
    })