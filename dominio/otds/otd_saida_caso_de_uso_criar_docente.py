from __future__ import annotations

from dataclasses import dataclass

from dominio.otds.otd_base import OTDBase
from dominio.entidades import Docente


@dataclass
class OTDSaidaCasoDeUsoCriarDocente(OTDBase):
    id: str
    nome: str

    @classmethod
    def de_entidade(cls, docente: Docente) -> OTDSaidaCasoDeUsoCriarDocente:
        return cls(
            id=str(docente.id.valor),
            nome=docente.nome.valor
        )
