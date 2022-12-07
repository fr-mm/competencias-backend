from __future__ import annotations

from dataclasses import dataclass
from typing import List
from uuid import UUID

from dominio.entidades import Modulo


@dataclass(frozen=True)
class OTDModulo:
    id: UUID
    numero: int
    disciplinas_ids: List[UUID]

    @classmethod
    def de_entidade(cls, modulo: Modulo) -> OTDModulo:
        return cls(
            id=modulo.id.valor,
            numero=modulo.numero.valor,
            disciplinas_ids=[id_.valor for id_ in modulo.disciplinas_ids],
        )

    def para_entidade(self) -> Modulo:
        return Modulo.construir(
            id_=self.id,
            numero=self.numero,
            disciplinas_ids=self.disciplinas_ids,
        )

