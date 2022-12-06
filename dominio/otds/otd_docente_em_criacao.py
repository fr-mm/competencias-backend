from dataclasses import dataclass
from typing import List
from uuid import UUID

from dominio.entidades import Docente


@dataclass(frozen=True)
class OTDDocenteEmCriacao:
    nome: str
    email: str
    telefones: List[str]
    tipo_de_contratacao: str
    unidade_senai_id: UUID

    def para_entidade(self) -> Docente:
        return Docente.construir(
            nome=self.nome,
            email=self.email,
            telefones=self.telefones,
            tipo_de_contratacao=self.tipo_de_contratacao,
            unidade_senai_id=self.unidade_senai_id,
        )
