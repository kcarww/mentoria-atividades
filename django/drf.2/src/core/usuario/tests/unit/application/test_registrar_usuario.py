import pytest

from core.usuario.application.registar_usuario_use_case import (
    RegistrarUsuarioInput,
    RegistrarUsuarioUseCase
)

class FakeUsuarioRepository:
    def __init__(self):
        self._usuarios = []

    def existe_email(self, email: str) -> bool:
        return any(u.email == email for u in self._usuarios)

    def salvar(self, usuario):
        self._usuarios.append(usuario)
        return usuario


def test_registrar_usuario_deve_registrar_com_sucesso():
    repo = FakeUsuarioRepository()
    use_case = RegistrarUsuarioUseCase(repo)

    input_dto = RegistrarUsuarioInput(
        nome="Ana",
        email="ana@email.com",
        senha="123456"
    )

    output = use_case.execute(input_dto)

    assert output.nome == "Ana"
    assert output.email == "ana@email.com"
    assert output.mensagem == "Usuário registrado com sucesso"
    assert output.id  # não vazio
    assert repo.existe_email("ana@email.com") is True


def test_registrar_usuario_deve_falhar_se_email_ja_existe():
    repo = FakeUsuarioRepository()
    use_case = RegistrarUsuarioUseCase(repo)

    use_case.execute(
        RegistrarUsuarioInput(nome="Ana", email="ana@email.com", senha="123456")
    )

    with pytest.raises(ValueError, match="Email já cadastrado"):
        use_case.execute(
            RegistrarUsuarioInput(nome="Outra", email="ana@email.com", senha="999999")
        )
