import re
from dataclasses import dataclass

from dominio.erros import ErroEmailInvalido


@dataclass(frozen=True)
class Email:
    valor: str

    def __post_init__(self) -> None:
        self.__validar()

    def __validar(self) -> None:
        padrao = r'^\w+(\.\w+)*@\w+(\.\w+)+$'
        if not re.match(padrao, self.valor):
            raise ErroEmailInvalido(self.valor)
