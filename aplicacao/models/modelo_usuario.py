from __future__ import annotations

from uuid import UUID

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy

from aplicacao.managers import UsuarioManager
from dominio.entidades import Usuario


class ModeloUsuario(AbstractUser):
    username = None
    nome = models.CharField(max_length=150)
    email = models.EmailField(gettext_lazy('email_address'), unique=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    @classmethod
    def de_entidade(cls, entidade: Usuario) -> ModeloUsuario:
        return cls(
            id=entidade.id.valor,
            nome=entidade.nome.valor,
            email=entidade.email.valor,
            is_active=entidade.ativo
        )

    def para_entidade(self) -> Usuario:
        return Usuario.construir(
            id_=UUID(str(self.id)),
            nome=str(self.nome),
            email=str(self.email),
            ativo=bool(self.is_active)
        )

    @property
    def ativo(self) -> bool:
        return self.is_active

    @ativo.setter
    def ativo(self, ativo: bool) -> None:
        self.is_active = ativo
