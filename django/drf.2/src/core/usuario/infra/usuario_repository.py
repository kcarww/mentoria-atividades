from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from core.usuario.domain.usuario import Usuario


class IUsuarioRepository(ABC):
    """Interface (porta) para repositório de usuários."""

    @abstractmethod
    def salvar(self, usuario: Usuario) -> Usuario:
        """Salva um usuário."""
        pass

    @abstractmethod
    def buscar_por_id(self, usuario_id: UUID) -> Optional[Usuario]:
        """Busca usuário por ID."""
        pass

    @abstractmethod
    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        """Busca usuário por email."""
        pass

    @abstractmethod
    def existe_email(self, email: str) -> bool:
        """Verifica se email já existe."""
        pass