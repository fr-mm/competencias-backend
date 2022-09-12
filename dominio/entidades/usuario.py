from __future__ import annotations

from uuid import UUID

from dominio.erros import ErroAoAtivarOuDesativarEntidade
from dominio.objetos_de_valor import IdDeUsuario, NomeDeUsuario, Email


class Usuario:
    __id: IdDeUsuario
    __nome: NomeDeUsuario
    __email: Email
    __ativo: bool

    def __init__(
            self,
            id_: IdDeUsuario,
            nome: NomeDeUsuario,
            email: Email,
            ativo: bool
    ) -> None:
        self.__id = id_
        self.__nome = nome
        self.__email = email
        self.__ativo = ativo

    @classmethod
    def construir(
            cls,
            id_: UUID,
            nome: str,
            email: str,
            ativo: bool
    ) -> Usuario:
        return cls(
            id_=IdDeUsuario(id_),
            nome=NomeDeUsuario(nome),
            email=Email(email),
            ativo=ativo
        )

    @property
    def id(self) -> IdDeUsuario:
        return self.__id

    @property
    def nome(self) -> NomeDeUsuario:
        return self.__nome

    @property
    def email(self) -> Email:
        return self.__email

    @property
    def ativo(self) -> bool:
        return self. __ativo

    def ativar(self) -> None:
        self.__mudar_ativo_para(True)

    def desativar(self) -> None:
        self.__mudar_ativo_para(False)

    def __mudar_ativo_para(self, novo_valor: bool) -> None:
        if self.ativo is novo_valor:
            raise ErroAoAtivarOuDesativarEntidade(
                nome_do_docente=self.nome.valor,
                id_do_docente=self.id.valor,
                tentou_mudar_ativo_para=novo_valor
            )
        self.__ativo = novo_valor
