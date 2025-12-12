from rest_framework import serializers
from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'estoque', 'ativo', 'criado_em']
        read_only_fields = ['id', 'criado_em']


class ProdutoListSerializer(serializers.ModelSerializer):
    """Serializer para listagem (campos resumidos)"""
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'estoque', 'ativo']


class ProdutoDetailSerializer(serializers.ModelSerializer):
    """Serializer para detalhes (todos os campos)"""
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'estoque', 'ativo', 'criado_em']
        read_only_fields = ['id', 'criado_em']


class ProdutoCreateSerializer(serializers.ModelSerializer):
    """Serializer para criação"""
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'ativo']

    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError("O preço deve ser maior que zero.")
        return value

    def validate_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("O estoque não pode ser negativo.")
        return value


class ProdutoUpdateSerializer(serializers.ModelSerializer):
    """Serializer para atualização completa (PUT)"""
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'ativo']

    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError("O preço deve ser maior que zero.")
        return value

    def validate_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("O estoque não pode ser negativo.")
        return value


class ProdutoPatchSerializer(serializers.ModelSerializer):
    """Serializer para atualização parcial (PATCH)"""
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'ativo']
        extra_kwargs = {
            'nome': {'required': False},
            'descricao': {'required': False},
            'preco': {'required': False},
            'estoque': {'required': False},
            'ativo': {'required': False},
        }

    def validate_preco(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("O preço deve ser maior que zero.")
        return value

    def validate_estoque(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("O estoque não pode ser negativo.")
        return value