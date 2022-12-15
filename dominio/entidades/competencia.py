from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from dominio.enums import NivelDeCompetenciaEnum
from dominio.objetos_de_valor import Id


@dataclass
class Competencia:
    docente_id: Id
    disciplina_id: Id
    nivel: NivelDeCompetenciaEnum

    @classmethod
    def construir(cls, docente_id: UUID, disciplina_id: UUID, nivel: int) -> Competencia:
        return cls(
            docente_id=Id(docente_id),
            disciplina_id=Id(disciplina_id),
            nivel=NivelDeCompetenciaEnum(nivel)
        )
