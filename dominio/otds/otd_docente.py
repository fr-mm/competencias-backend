from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from dominio.entidades import Docente


@dataclass
class OTDDocente:
    id: UUID
    nome: str

    @classmethod
    def de_entidade(cls, docente: Docente) -> OTDDocente:
        return cls(
            id=docente.id.valor,
            nome=docente.nome.valor
        )

    def para_entidade(self) -> Docente:
        return Docente.construir(
            id_=self.id,
            nome=self.nome
        )
