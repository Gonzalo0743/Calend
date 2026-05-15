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
    bot_id = None
    if hasattr(user, 'bot'):
        bot_id = user.bot.id
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_staff': user.is_staff,
        'role': 'admin' if user.is_staff else 'client',
        'bot_id': bot_id,
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

# --- Usuarios clientes ---

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def clientes_list(request):
    usuarios = User.objects.filter(is_staff=False)
    data = [{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'tiene_bot': hasattr(u, 'bot'),
        'bot_id': u.bot.id if hasattr(u, 'bot') else None,
        'bot_nombre': u.bot.nombre if hasattr(u, 'bot') else None,
    } for u in usuarios]
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_cliente(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    bot_id = request.data.get('bot_id')

    if not username or not email or not password:
        return Response(
            {'error': 'Username, email y password son requeridos'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {'error': 'Ya existe un usuario con ese email'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        is_staff=False
    )

    if bot_id:
        try:
            bot = Bot.objects.get(pk=bot_id)
            bot.usuario = user
            bot.save()
        except Bot.DoesNotExist:
            pass

    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'bot_id': bot_id,
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def asignar_bot(request):
    user_id = request.data.get('user_id')
    bot_id = request.data.get('bot_id')

    if not user_id or not bot_id:
        return Response(
            {'error': 'user_id y bot_id son requeridos'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = User.objects.get(pk=user_id)
        bot = Bot.objects.get(pk=bot_id)

        # Desasignar bot anterior si lo tiene
        Bot.objects.filter(usuario=user).update(usuario=None)

        bot.usuario = user
        bot.save()

        return Response({'message': 'Bot asignado correctamente'})
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Bot.DoesNotExist:
        return Response({'error': 'Bot no encontrado'}, status=status.HTTP_404_NOT_FOUND)