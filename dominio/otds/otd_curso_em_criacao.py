from __future__ import annotations

from dataclasses import dataclass
from typing import List

from dominio.entidades import Curso
from dominio.otds import OTDModuloEmCriacao


@dataclass(frozen=True)
class OTDCursoEmCriacao:
    nome: str
    modulos: List[OTDModuloEmCriacao]
    ativo: bool

    def para_entidade(self) -> Curso:
        return Curso.construir(
            nome=self.nome,
            modulos=[otd.para_entidade() for otd in self.modulos],
            ativo=self.ativo
        )
