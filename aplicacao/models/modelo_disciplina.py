from __future__ import annotations

from uuid import UUID

from django.db import models

from dominio.entidades import Disciplina


class ModeloDisciplina(models.Model):
    id = models.UUIDField(primary_key=True)
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    ativo = models.BooleanField()

    def para_entidade(self) -> Disciplina:
        return Disciplina.construir(
            id_=UUID(str(self.id)),
            nome=str(self.nome),
            carga_horaria=int(str(self.carga_horaria)),
            ativo=bool(self.ativo)
        )

    @classmethod
    def de_entidade(cls, entidade: Disciplina) -> ModeloDisciplina:
        return cls(
            id=entidade.id.valor,
            nome=entidade.nome.valor,
            carga_horaria=entidade.carga_horaria.valor,
            ativo=entidade.ativo
        )
