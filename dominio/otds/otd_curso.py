from __future__ import annotations

from dataclasses import dataclass
from typing import List
from uuid import UUID

from dominio.entidades import Curso


@dataclass(frozen=True)
class OTDCurso:
    id: UUID
    nome: str
    modulos_ids: List[UUID]
    ativo: bool

    @classmethod
    def de_entidade(cls, curso: Curso) -> OTDCurso:
        return cls(
            id=curso.id.valor,
            nome=curso.nome.valor,
            modulos_ids=[id_.valor for id_ in curso.modulos_ids],
            ativo=curso.ativo
        )

    def para_entidade(self) -> Curso:
        return Curso.construir(
            id_=self.id,
            nome=self.nome,
            modulos_ids=self.modulos_ids,
            ativo=self.ativo
        )
