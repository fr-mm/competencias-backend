from __future__ import annotations
from dominio.enums import TipoDeContratacaoEnum
from dominio.erros import ErroTipoDeContratacao


class TipoDeContratacao:
    __valor: TipoDeContratacaoEnum

    def __init__(self, valor: str) -> None:
        try:
            self.__valor = TipoDeContratacaoEnum(valor)
        except ValueError:
            raise ErroTipoDeContratacao(valor)

    @property
    def valor(self) -> TipoDeContratacaoEnum:
        return self.__valor

    def __eq__(self, outro: TipoDeContratacao) -> bool:
        return self.valor == outro.valor
