from __future__ import annotations

from dataclasses import dataclass
from typing import List
from uuid import UUID

from dominio.entidades import Curso
from dominio.otds.otd_modulo import OTDModulo


@dataclass
class OTDCursoSaida:
    id: UUID
    nome: str
    modulos: List[OTDModulo]
    ativo: bool

    @classmethod
    def de_entidade(cls, curso: Curso) -> OTDCursoSaida:
        return cls(
            id=curso.id.valor,
            nome=curso.nome.valor,
            modulos=[OTDModulo.de_entidade(modulo) for modulo in curso.modulos],
            ativo=curso.ativo
        )
