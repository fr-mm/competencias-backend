from __future__ import annotations

from dataclasses import dataclass

from dominio.entidades import Disciplina


@dataclass(frozen=True)
class OTDDisciplinaEmCriacao:
    nome: str
    carga_horaria: int

    def para_entidade(self) -> Disciplina:
        return Disciplina.construir(
            nome=self.nome,
            carga_horaria=self.carga_horaria,
            ativo=True
        )

