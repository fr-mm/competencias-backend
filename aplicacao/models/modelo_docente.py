from __future__ import annotations

from uuid import UUID

from django.db import models

from dominio.entidades import Docente


class ModeloDocente(models.Model):
    nome = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, unique=True)

    @classmethod
    def de_entidade(cls, entidade: Docente) -> ModeloDocente:
        return cls(
            nome=entidade.nome.valor,
            id=entidade.id.valor
        )

    def para_entidade(self) -> Docente:
        return Docente.construir(
            nome=str(self.nome),
            id_=UUID(str(self.id))
        )
