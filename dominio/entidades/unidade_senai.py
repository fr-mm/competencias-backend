from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from dominio.objetos_de_valor import NomeUnidadeSenai, Id


@dataclass(frozen=True)
class UnidadeSenai:
    id: Id
    nome: NomeUnidadeSenai

    @classmethod
    def construir(cls, id_: UUID, nome: str) -> UnidadeSenai:
        return cls(
            id=Id(id_),
            nome=NomeUnidadeSenai(nome)
        )
