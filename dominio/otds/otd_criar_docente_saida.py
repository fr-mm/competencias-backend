from __future__ import annotations

from dataclasses import dataclass

from dominio.entidades import Docente


@dataclass
class OTDCriarDocenteSaida:
    id: str
    nome: str

    @classmethod
    def de_entidade(cls, docente: Docente) -> OTDCriarDocenteSaida:
        return cls(
            id=str(docente.id.valor),
            nome=docente.nome.valor
        )
