from __future__ import annotations

from uuid import UUID

from django.contrib.auth.models import User
from django.db import models

from dominio.entidades import Usuario


class ModeloUsuario(User):
    @classmethod
    def de_entidade(cls, entidade: Usuario) -> ModeloUsuario:
        return cls(
            id=entidade.id.valor,
            username=entidade.nome.valor,
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
    def nome(self) -> str:
        return self.username

    @nome.setter
    def nome(self, nome: str) -> None:
        self.username = nome

    @property
    def ativo(self) -> bool:
        return self.is_active

    @ativo.setter
    def ativo(self, ativo: bool) -> None:
        self.is_active = ativo
