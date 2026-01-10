import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_registrar_usuario_view_sucesso(monkeypatch):
    client = APIClient()

    url = "/api/usuarios/registrar/"

    class FakeOutput:
        id = "uuid-123"
        nome = "Ana"
        email = "ana@email.com"
        mensagem = "Usuário registrado com sucesso"

    def fake_execute(self, input_data):
        return FakeOutput()

    monkeypatch.setattr(
        "django_api.usuario.views.RegistrarUsuarioUseCase.execute",
        fake_execute
    )

    payload = {
        "nome": "Ana",
        "email": "ana@email.com",
        "senha": "123456"
    }

    res = client.post(url, payload, format="json")

    assert res.status_code == 201
    assert res.data["id"] == "uuid-123"
    assert res.data["nome"] == "Ana"
    assert res.data["email"] == "ana@email.com"
    assert "mensagem" in res.data


@pytest.mark.django_db
def test_registrar_usuario_view_payload_invalido():
    client = APIClient()
    url = "/api/usuarios/registrar/"

    payload = {
        "nome": "",  
        "email": "ana@email.com",
        "senha": "123456"
    }

    res = client.post(url, payload, format="json")

    assert res.status_code == 400


@pytest.mark.django_db
def test_registrar_usuario_view_email_ja_cadastrado(monkeypatch):
    client = APIClient()
    url = "/api/usuarios/registrar/"

    def fake_execute(self, input_data):
        raise ValueError("Email já cadastrado")

    monkeypatch.setattr(
        "django_api.usuario.views.RegistrarUsuarioUseCase.execute",
        fake_execute
    )

    payload = {
        "nome": "Ana",
        "email": "ana@email.com",
        "senha": "123456"
    }

    res = client.post(url, payload, format="json")

    assert res.status_code == 400
    assert res.data["error"] == "Email já cadastrado"
