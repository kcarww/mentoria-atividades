from django.db import models
import uuid


class UsuarioModel(models.Model):
    """Model Django para persistência de usuários."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    senha_hash = models.CharField(max_length=64)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "usuarios"
        ordering = ["-data_criacao"]
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.email