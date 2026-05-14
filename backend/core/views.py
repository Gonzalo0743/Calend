from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

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

    # Intentar buscar por email
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

    login(request, user)

    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_staff': user.is_staff,
        'role': 'admin' if user.is_staff else 'client',
    })
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
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