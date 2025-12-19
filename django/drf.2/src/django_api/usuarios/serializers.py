from rest_framework import serializers


class RegistrarUsuarioSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    senha = serializers.CharField(write_only=True, min_length=6)


class AutenticarUsuarioSerializer(serializers.Serializer):
    email = serializers.EmailField()
    senha = serializers.CharField(write_only=True)


class UsuarioResponseSerializer(serializers.Serializer):
    id = serializers.CharField()
    nome = serializers.CharField()
    email = serializers.EmailField()
    mensagem = serializers.CharField()