from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Produto
from .serializers import (
    ProdutoListSerializer,
    ProdutoDetailSerializer,
    ProdutoCreateSerializer,
    ProdutoUpdateSerializer,
    ProdutoPatchSerializer,
)


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()

    def get_serializer_class(self):
        """Retorna o serializer apropriado para cada ação"""
        if self.action == 'list':
            return ProdutoListSerializer
        elif self.action == 'retrieve':
            return ProdutoDetailSerializer
        elif self.action == 'create':
            return ProdutoCreateSerializer
        elif self.action == 'update':
            return ProdutoUpdateSerializer
        elif self.action == 'partial_update':
            return ProdutoPatchSerializer
        return ProdutoDetailSerializer

    def list(self, request):
        """GET /api/produtos/ - Listar todos os produtos"""
        produtos = self.get_queryset()
        serializer = self.get_serializer(produtos, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST /api/produtos/ - Criar um novo produto"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """GET /api/produtos/{id}/ - Buscar um produto específico"""
        produto = self.get_object()
        serializer = self.get_serializer(produto)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """PUT /api/produtos/{id}/ - Atualizar completamente um produto"""
        produto = self.get_object()
        serializer = self.get_serializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """PATCH /api/produtos/{id}/ - Atualizar parcialmente um produto"""
        produto = self.get_object()
        serializer = self.get_serializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """DELETE /api/produtos/{id}/ - Deletar um produto"""
        produto = self.get_object()
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)