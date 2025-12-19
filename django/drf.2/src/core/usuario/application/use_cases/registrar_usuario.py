from dataclasses import dataclass
from core.usuario.domain.usuario import Usuario
from core.usuario.infra.usuario_repository import IUsuarioRepository

@dataclass
class RegistrarUsuarioInput:
    nome: str
    email: str
    senha: str


@dataclass
class RegistrarUsuarioOutput:
    id: str
    nome: str
    email: str
    mensagem: str


class RegistrarUsuarioUseCase:
    """Caso de uso: Registrar novo usuário."""

    def __init__(self, repository: IUsuarioRepository):
        self.repository = repository

    def execute(self, input_dto: RegistrarUsuarioInput) -> RegistrarUsuarioOutput:
        """Executa o caso de uso."""
        
        # Regra de negócio: email deve ser único
        if self.repository.existe_email(input_dto.email):
            raise ValueError("Email já cadastrado")

        # Cria entidade de domínio
        usuario = Usuario.criar(
            nome=input_dto.nome,
            email=input_dto.email,
            senha=input_dto.senha
        )

        # Persiste
        usuario_salvo = self.repository.salvar(usuario)

        # Retorna DTO de saída
        return RegistrarUsuarioOutput(
            id=str(usuario_salvo.id),
            nome=usuario_salvo.nome,
            email=usuario_salvo.email,
            mensagem="Usuário registrado com sucesso"
        )