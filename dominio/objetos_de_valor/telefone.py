from __future__ import annotations
import re

from dominio.erros.erro_telefone import ErroTelefone


class Telefone:
    __valor: str
    __padrao = r"^\(\d{2}\)\d{4,5}-\d{4}$"

    def __init__(self, valor: str) -> None:
        self.__validar(valor)
        self.__valor = valor

    @property
    def valor(self) -> str:
        return self.__valor

    def __validar(self, valor: str) -> None:
        if not re.match(self.__padrao, valor):
            raise ErroTelefone(valor)

    def __eq__(self, outro: Telefone) -> bool:
        return self.valor == outro.valor
