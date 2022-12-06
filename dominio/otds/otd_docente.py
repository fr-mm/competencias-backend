from __future__ import annotations

from dataclasses import dataclass
from typing import List
from uuid import UUID

from dominio.entidades import Docente


@dataclass(frozen=True)
class OTDDocente:
    id: UUID
    nome: str
    email: str
    telefones: List[str]
    tipo_de_contratacao: str
    unidade_senai_id: UUID
    ativo: bool

    @classmethod
    def de_entidade(cls, docente: Docente) -> OTDDocente:
        return cls(
            id=docente.id.valor,
            nome=docente.nome.valor,
            email=docente.email.valor,
            telefones=[telefone.valor for telefone in docente.telefones],
            tipo_de_contratacao=str(docente.tipo_de_contratacao.valor.value),
            unidade_senai_id=docente.unidade_senai_id.valor,
            ativo=docente.ativo
        )

    def para_entidade(self) -> Docente:
        return Docente.construir(
            id_=self.id,
            nome=self.nome,
            email=self.email,
            telefones=self.telefones,
            tipo_de_contratacao=self.tipo_de_contratacao,
            unidade_senai_id=self.unidade_senai_id,
            ativo=self.ativo
        )
