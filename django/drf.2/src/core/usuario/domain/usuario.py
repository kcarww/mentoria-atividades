from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
import hashlib


@dataclass
class Usuario:
    """Entidade de domínio Usuario."""
    
    id: UUID = field(default_factory=uuid4)
    nome: str = ""
    email: str = ""
    senha_hash: str = ""
    data_criacao: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validações de domínio."""
        if not self.nome or len(self.nome.strip()) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")
        
        if not self.email or "@" not in self.email:
            raise ValueError("Email inválido")
        
        if not self.senha_hash:
            raise ValueError("Senha não pode ser vazia")

    @staticmethod
    def hash_senha(senha: str) -> str:
        """Gera hash da senha."""
        return hashlib.sha256(senha.encode()).hexdigest()

    def verificar_senha(self, senha: str) -> bool:
        """Verifica se a senha está correta."""
        return self.senha_hash == self.hash_senha(senha)

    @classmethod
    def criar(cls, nome: str, email: str, senha: str) -> "Usuario":
        """Factory method para criar usuário com senha já hasheada."""
        return cls(
            nome=nome.strip(),
            email=email.strip().lower(),
            senha_hash=cls.hash_senha(senha)
        )