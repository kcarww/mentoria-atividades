from typing import Optional
from uuid import UUID

from core.usuario.domain.usuario import Usuario
from core.usuario.infra.usuario_repository import IUsuarioRepository
from django_api.usuarios.models import UsuarioModel


class UsuarioRepositoryDjango(IUsuarioRepository):
    """Implementação Django ORM do repositório de usuários."""

    def salvar(self, usuario: Usuario) -> Usuario:
        """Salva usuário no banco via Django ORM."""
        usuario_model = UsuarioModel.objects.create(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha_hash=usuario.senha_hash
        )
        return self._to_domain(usuario_model)

    def buscar_por_id(self, usuario_id: UUID) -> Optional[Usuario]:
        """Busca por ID."""
        try:
            usuario_model = UsuarioModel.objects.get(id=usuario_id)
            return self._to_domain(usuario_model)
        except UsuarioModel.DoesNotExist:
            return None

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        """Busca por email."""
        try:
            usuario_model = UsuarioModel.objects.get(email=email.lower().strip())
            return self._to_domain(usuario_model)
        except UsuarioModel.DoesNotExist:
            return None

    def existe_email(self, email: str) -> bool:
        """Verifica se email existe."""
        return UsuarioModel.objects.filter(email=email.lower().strip()).exists()

    @staticmethod
    def _to_domain(model: UsuarioModel) -> Usuario:
        """Converte Django Model para entidade de domínio."""
        return Usuario(
            id=model.id,
            nome=model.nome,
            email=model.email,
            senha_hash=model.senha_hash,
            data_criacao=model.data_criacao
        )