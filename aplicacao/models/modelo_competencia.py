from __future__ import annotations

from uuid import UUID

from django.db import models

from aplicacao.models import ModeloDocente, ModeloDisciplina
from dominio.entidades import Competencia


class ModeloCompetencia(models.Model):
    docente = models.ForeignKey(ModeloDocente, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(ModeloDisciplina, on_delete=models.CASCADE)
    nivel = models.IntegerField()

    @classmethod
    def de_entidade(cls, competencia: Competencia) -> ModeloCompetencia:
        return cls(
            docente=ModeloDocente.objects.get(pk=competencia.docente_id.valor),
            disciplina=ModeloDisciplina.objects.get(pk=competencia.disciplina_id.valor),
            nivel=competencia.nivel.value
        )

    def para_entidade(self) -> Competencia:
        return Competencia.construir(
            docente_id=UUID(str(self.docente.id)),
            disciplina_id=UUID(str(self.disciplina.id)),
            nivel=int(str(self.nivel))
        )
