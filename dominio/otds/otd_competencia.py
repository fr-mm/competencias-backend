from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from dominio.entidades import Competencia


@dataclass
class OTDCompetencia:
    docente_id: UUID
    disciplina_id: UUID
    nivel: int

    @classmethod
    def de_entidade(cls, competencia: Competencia) -> OTDCompetencia:
        return cls(
            docente_id=competencia.docente_id.valor,
            disciplina_id=competencia.disciplina_id.valor,
            nivel=competencia.nivel.value
        )

    def para_entidade(self) -> Competencia:
        return Competencia.construir(
            docente_id=self.docente_id,
            disciplina_id=self.disciplina_id,
            nivel=self.nivel
        )
