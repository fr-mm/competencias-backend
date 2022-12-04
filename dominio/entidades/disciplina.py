from __future__ import annotations

from uuid import UUID

from dominio.erros import ErroAoAtivarDesativarEntidade
from dominio.objetos_de_valor import Id, NomeDeDisciplina, CargaHoraria


class Disciplina:
    __id: Id
    __nome: NomeDeDisciplina
    __carga_horaria: CargaHoraria
    __ativo: bool

    def __init__(self, id_: Id, nome: NomeDeDisciplina, carga_horaria: CargaHoraria, ativo: bool) -> None:
        self.__id = id_
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        self.__ativo = ativo

    @classmethod
    def construir(cls, id_: UUID, nome: str, carga_horaria: int, ativo: bool) -> Disciplina:
        return Disciplina(
            id_=Id(id_),
            nome=NomeDeDisciplina(nome),
            carga_horaria=CargaHoraria(carga_horaria),
            ativo=ativo
        )

    @property
    def id(self) -> Id:
        return self.__id

    @property
    def nome(self) -> NomeDeDisciplina:
        return self.__nome

    @property
    def carga_horaria(self) -> CargaHoraria:
        return self.__carga_horaria

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
