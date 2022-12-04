from __future__ import annotations

from typing import List
from uuid import UUID

from dominio.erros import ErroAoAtivarDesativarEntidade
from dominio.objetos_de_valor import Id, NumeroDeModulo


class Modulo:
    __id: Id
    __numero: NumeroDeModulo
    __disciplinas_ids: List[Id]
    __ativo: bool

    def __init__(
            self,
            id_: Id,
            numero: NumeroDeModulo,
            disciplinas_ids: List[Id],
            ativo: bool = True
    ) -> None:
        self.__id = id_
        self.__numero = numero
        self.__disciplinas_ids = disciplinas_ids
        self.__ativo = ativo

    @classmethod
    def construir(
            cls,
            id_: UUID,
            numero: int,
            disciplinas_ids: List[Id],
            ativo: bool
    ) -> Modulo:
        return cls(
            id_=Id(id_),
            numero=NumeroDeModulo(numero),
            disciplinas_ids=disciplinas_ids,
            ativo=ativo
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

    @property
    def ativo(self) -> bool:
        return self.__ativo

    def ativar(self) -> None:
        self.__mudar_ativo_para(True)

    def desativar(self) -> None:
        self.__mudar_ativo_para(False)

    def __mudar_ativo_para(self, novo_valor: bool) -> None:
        if self.ativo is novo_valor:
            raise ErroAoAtivarDesativarEntidade(
                nome_da_entidade=f'Módulo {self.numero}',
                id_da_entidade=self.id.valor,
                tentou_mudar_ativo_para=novo_valor
            )
        self.__ativo = novo_valor
