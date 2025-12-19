from dataclasses import dataclass
from core.usuario.infra.usuario_repository import IUsuarioRepository

@dataclass
class AutenticarUsuarioInput:
    email: str
    senha: str


@dataclass
class AutenticarUsuarioOutput:
    id: str
    nome: str
    email: str
    mensagem: str


class AutenticarUsuarioUseCase:
    """Caso de uso: Autenticar usuário."""

    def __init__(self, repository: IUsuarioRepository):
        self.repository = repository

    def execute(self, input_dto: AutenticarUsuarioInput) -> AutenticarUsuarioOutput:
        """Executa o caso de uso."""
        
        # Busca usuário por email
        usuario = self.repository.buscar_por_email(input_dto.email)
        
        if not usuario:
            raise ValueError("Credenciais inválidas")

        # Verifica senha
        if not usuario.verificar_senha(input_dto.senha):
            raise ValueError("Credenciais inválidas")

        # Retorna dados do usuário autenticado
        return AutenticarUsuarioOutput(
            id=str(usuario.id),
            nome=usuario.nome,
            email=usuario.email,
            mensagem="Autenticação realizada com sucesso"
        )