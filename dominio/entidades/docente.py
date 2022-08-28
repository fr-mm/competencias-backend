from __future__ import annotations

from uuid import UUID, uuid4

from dominio.objetos_de_valor import NomeDeDocente, IdDeDocente


class Docente:
    __nome: NomeDeDocente
    __id: IdDeDocente
    __ativo: bool

    def __init__(
            self,
            nome: NomeDeDocente,
            id_: IdDeDocente,
            ativo: bool
    ) -> None:
        self.__nome = nome
        self.__id = id_
        self.__ativo = ativo

    @property
    def nome(self) -> NomeDeDocente:
        return self.__nome

    @property
    def id(self) -> IdDeDocente:
        return self.__id

    @property
    def ativo(self) -> bool:
        return self.__ativo

    @classmethod
    def construir(cls, nome: str, id_: UUID = uuid4(), ativo: bool = True) -> Docente:
        return cls(
            nome=NomeDeDocente(nome),
            id_=IdDeDocente(id_),
            ativo=ativo
        )
