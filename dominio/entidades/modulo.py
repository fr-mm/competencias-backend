from __future__ import annotations

from typing import List
from uuid import UUID, uuid4

from dominio.objetos_de_valor import Id, NumeroDeModulo


class Modulo:
    __id: Id
    __numero: NumeroDeModulo
    __disciplinas_ids: List[Id]

    def __init__(
            self,
            id_: Id,
            numero: NumeroDeModulo,
            disciplinas_ids: List[Id],
    ) -> None:
        self.__id = id_
        self.__numero = numero
        self.__disciplinas_ids = disciplinas_ids

    @classmethod
    def construir(
            cls,
            numero: int,
            disciplinas_ids: List[UUID],
            id_: UUID = uuid4(),
    ) -> Modulo:
        return cls(
            id_=Id(id_),
            numero=NumeroDeModulo(numero),
            disciplinas_ids=[Id(id_) for id_ in disciplinas_ids],
        )

    @property
    def id(self) -> Id:
        return self.__id

    @property
    def numero(self) -> NumeroDeModulo:
        return self.__numero

    @property
    def disciplinas_ids(self) -> List[Id]:
        return self.__disciplinas_ids
