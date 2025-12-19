from typing import Optional, Dict
from uuid import UUID
from core.usuario.domain.usuario import Usuario
from core.usuario.infra.usuario_repository import IUsuarioRepository


class UsuarioRepositoryMemory(IUsuarioRepository):
    """Implementação em memória do repositório de usuários."""

    def __init__(self):
        self._usuarios: Dict[UUID, Usuario] = {}

    def salvar(self, usuario: Usuario) -> Usuario:
        """Salva usuário em memória."""
        self._usuarios[usuario.id] = usuario
        return usuario

    def buscar_por_id(self, usuario_id: UUID) -> Optional[Usuario]:
        """Busca por ID."""
        return self._usuarios.get(usuario_id)

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        """Busca por email."""
        email_lower = email.lower().strip()
        for usuario in self._usuarios.values():
            if usuario.email == email_lower:
                return usuario
        return None

    def existe_email(self, email: str) -> bool:
        """Verifica se email existe."""
        return self.buscar_por_email(email) is not None
    

if __name__ == "__main__":
    # Exemplo de uso do repositório em memória
    repo = UsuarioRepositoryMemory()
    usuario = Usuario.criar(nome="João Silva", email="heheh@gmail.com", senha="senha123")
    repo.salvar(usuario)
    encontrado = repo.buscar_por_email("heheh@gmail.com")
    print(encontrado)  # Deve imprimir os dados do usuário salvo