from django.urls import path
from django_api.usuarios.views import RegistrarUsuarioView, AutenticarUsuarioView

app_name = 'usuarios'

urlpatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/', AutenticarUsuarioView.as_view(), name='login'),
]