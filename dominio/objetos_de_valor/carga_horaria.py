from __future__ import annotations

from dominio.objetos_de_valor import NumeroMaiorQueZero


class CargaHoraria:
    __valor: NumeroMaiorQueZero

    def __init__(self, valor: int) -> None:
        self.__valor = NumeroMaiorQueZero(
            valor=valor,
            maximo=1000000
        )

    @property
    def valor(self) -> int:
        return self.__valor.valor

    def __eq__(self, outro: CargaHoraria) -> bool:
        return self.valor == outro.valor
