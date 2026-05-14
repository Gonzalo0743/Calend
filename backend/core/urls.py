from django.urls import path
from . import views

urlpatterns = [
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/me/', views.me_view, name='me'),

    path('bots/', views.bots_list, name='bots-list'),
    path('bots/<int:pk>/', views.bot_detail, name='bot-detail'),

    path('citas/', views.citas_list, name='citas-list'),
    path('citas/<int:pk>/', views.cita_detail, name='cita-detail'),

    path('contactos/', views.contactos_list, name='contactos-list'),

    path('metricas/', views.metricas, name='metricas'),
]