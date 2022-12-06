from __future__ import annotations

from dataclasses import dataclass
from typing import List
from uuid import UUID

from dominio.entidades import Curso


@dataclass(frozen=True)
class OTDCursoEmCriacao:
    nome: str
    modulos_ids: List[UUID]
    ativo: bool

    def para_entidade(self) -> Curso:
        return Curso.construir(
            nome=self.nome,
            modulos_ids=self.modulos_ids,
            ativo=self.ativo
        )
