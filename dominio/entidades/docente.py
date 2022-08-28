from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4

from dominio.objetos_de_valor import NomeDeDocente, IdDeDocente


@dataclass(frozen=True)
class Docente:
    nome: NomeDeDocente
    id: IdDeDocente
    ativo: bool

    @classmethod
    def construir(cls, nome: str, id_: UUID = uuid4(), ativo: bool = True) -> Docente:
        return cls(
            nome=NomeDeDocente(nome),
            id=IdDeDocente(id_),
            ativo=ativo
        )
