from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_api.usuarios.serializers import (
    RegistrarUsuarioSerializer,
    AutenticarUsuarioSerializer,
    UsuarioResponseSerializer
)
from core.usuario.application.use_cases.registrar_usuario import (
    RegistrarUsuarioUseCase,
    RegistrarUsuarioInput
)
from core.usuario.application.use_cases.autenticar_usuario import (
    AutenticarUsuarioUseCase,
    AutenticarUsuarioInput
)
from django_api.usuarios.repository import UsuarioRepositoryDjango


class RegistrarUsuarioView(APIView):
    """Endpoint para registrar novo usuário."""

    def post(self, request):
        serializer = RegistrarUsuarioSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Instancia repositório Django e caso de uso
            repository = UsuarioRepositoryDjango()
            use_case = RegistrarUsuarioUseCase(repository)

            # Executa caso de uso
            input_dto = RegistrarUsuarioInput(**serializer.validated_data)
            output_dto = use_case.execute(input_dto)

            # Serializa resposta
            response_serializer = UsuarioResponseSerializer(output_dto)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"erro": "Erro interno do servidor"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AutenticarUsuarioView(APIView):
    """Endpoint para autenticar usuário (login)."""

    def post(self, request):
        serializer = AutenticarUsuarioSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Instancia repositório Django e caso de uso
            repository = UsuarioRepositoryDjango()
            use_case = AutenticarUsuarioUseCase(repository)

            # Executa caso de uso
            input_dto = AutenticarUsuarioInput(**serializer.validated_data)
            output_dto = use_case.execute(input_dto)

            # Serializa resposta
            response_serializer = UsuarioResponseSerializer(output_dto)
            return Response(response_serializer.data, status=status.HTTP_200_OK)

        except ValueError as e:
            return Response({"erro": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(
                {"erro": "Erro interno do servidor"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )