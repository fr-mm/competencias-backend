from __future__ import annotations

from typing import List
from uuid import UUID

from dominio.erros import ErroAoAtivarDesativarEntidade
from dominio.objetos_de_valor import Id, NomeDeCurso


class Curso:
    __id: Id
    __nome: NomeDeCurso
    __modulos_ids: List[Id]
    __ativo: bool

    def __init__(
            self,
            id_: Id,
            nome: NomeDeCurso,
            modulos_ids: List[Id],
            ativo: bool
    ) -> None:
        self.__id = id_
        self.__nome = nome
        self.__modulos_ids = modulos_ids
        self.__ativo = ativo

    @classmethod
    def construir(
            cls,
            id_: UUID,
            nome: str,
            modulos_ids: List[Id],
            ativo: bool
    ) -> Curso:
        return cls(
            id_=Id(id_),
            nome=NomeDeCurso(nome),
            modulos_ids=modulos_ids,
            ativo=ativo
        )

    @property
    def id(self) -> Id:
        return self.__id

    @property
    def nome(self) -> NomeDeCurso:
        return self.__nome

    @property
    def modulos(self) -> List[Id]:
        return self.__modulos_ids

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
                nome_da_entidade=self.nome.valor,
                id_da_entidade=self.id.valor,
                tentou_mudar_ativo_para=novo_valor
            )
        self.__ativo = novo_valor
