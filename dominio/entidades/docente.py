from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4

from dominio.objetos_de_valor import NomeDeDocente, IdDeDocente


@dataclass(frozen=True)
class Docente:
    nome: NomeDeDocente
    id: IdDeDocente

    @classmethod
    def construir(cls, nome: str, id_: UUID = uuid4()) -> Docente:
        return cls(
            nome=NomeDeDocente(nome),
            id=IdDeDocente(id_)
        )
