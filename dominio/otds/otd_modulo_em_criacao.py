from __future__ import annotations

from dataclasses import dataclass
from typing import List
from uuid import UUID

from dominio.entidades import Modulo


@dataclass(frozen=True)
class OTDModuloEmCriacao:
    numero: int
    disciplinas_ids: List[UUID]
    ativo: bool

    def para_entidade(self) -> Modulo:
        return Modulo.construir(
            numero=self.numero,
            disciplinas_ids=self.disciplinas_ids,
            ativo=self.ativo
        )

