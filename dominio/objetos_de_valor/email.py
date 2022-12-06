from __future__ import annotations
import re

from dominio.erros import ErroEmail


class Email:
    __valor: str
    __padrao = r"^([\w.\-_]+(@)([\w\d]+)(.[\w\d]+)+)$"

    def __init__(self, valor: str) -> None:
        self.__validar(valor)
        self.__valor = valor

    @property
    def valor(self) -> str:
        return self.__valor

    def __validar(self, valor: str) -> None:
        if not re.match(self.__padrao, valor):
            raise ErroEmail(valor)

    def __eq__(self, outro: Email) -> bool:
        return self.valor == outro.valor
