from __future__ import annotations

from uuid import UUID

from django.db import models

from dominio.entidades import UnidadeSenai


class ModeloUnidadeSenai(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    nome = models.CharField(max_length=200)

    @classmethod
    def de_entidade(cls, entidade: UnidadeSenai) -> ModeloUnidadeSenai:
        return cls(
            id=entidade.id.valor,
            nome=entidade.nome.valor
        )

    def para_entidade(self) -> UnidadeSenai:
        return UnidadeSenai.construir(
            id_=UUID(str(self.id)),
            nome=str(self.nome)
        )
