from __future__ import annotations

from typing import List
from uuid import UUID, uuid4

from dominio.erros import ErroAoAtivarDesativarEntidade
from dominio.objetos_de_valor import Email, Telefone, TipoDeContratacao
from dominio.objetos_de_valor import NomeDeDocente, Id


class Docente:
    __nome: NomeDeDocente
    __id: Id
    __email: Email
    __telefones: List[Telefone]
    __tipo_de_contratacao: TipoDeContratacao
    __unidade_senai_id: Id
    __ativo: bool

    def __init__(
            self,
            nome: NomeDeDocente,
            id_: Id,
            email: Email,
            telefones: List[Telefone],
            tipo_de_contratacao: TipoDeContratacao,
            unidade_senai_id: Id,
            ativo: bool
    ) -> None:
        self.__nome = nome
        self.__id = id_
        self.__email = email
        self.__telefones = telefones
        self.__tipo_de_contratacao = tipo_de_contratacao
        self.__unidade_senai_id = unidade_senai_id
        self.__ativo = ativo

    @classmethod
    def construir(
            cls,
            nome: str,
            email: str,
            telefones: List[str],
            tipo_de_contratacao: str,
            unidade_senai_id: UUID,
            id_: UUID = uuid4(),
            ativo: bool = True
    ) -> Docente:
        return cls(
            nome=NomeDeDocente(nome),
            id_=Id(id_),
            email=Email(email),
            telefones=[Telefone(telefone) for telefone in telefones],
            tipo_de_contratacao=TipoDeContratacao(tipo_de_contratacao),
            unidade_senai_id=Id(unidade_senai_id),
            ativo=ativo
        )

    @property
    def nome(self) -> NomeDeDocente:
        return self.__nome

    @property
    def id(self) -> Id:
        return self.__id

    @property
    def email(self) -> Email:
        return self.__email

    @property
    def telefones(self) -> List[Telefone]:
        return self.__telefones

    @property
    def tipo_de_contratacao(self) -> TipoDeContratacao:
        return self.__tipo_de_contratacao

    @property
    def unidade_senai_id(self) -> Id:
        return self.__unidade_senai_id

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
