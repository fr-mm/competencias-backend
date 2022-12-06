from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from dominio.entidades import Disciplina


@dataclass(frozen=True)
class OTDDisciplina:
    id: UUID
    nome: str
    carga_horaria: int
    ativo: bool

    @classmethod
    def de_entidade(cls, disciplina: Disciplina) -> OTDDisciplina:
        return cls(
            id=disciplina.id.valor,
            nome=disciplina.nome.valor,
            carga_horaria=disciplina.carga_horaria.valor,
            ativo=disciplina.ativo
        )

    def para_entidade(self) -> Disciplina:
        return Disciplina.construir(
            id_=self.id,
            nome=self.nome,
            carga_horaria=self.carga_horaria,
            ativo=self.ativo
        )

