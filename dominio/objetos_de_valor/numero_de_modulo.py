from __future__ import annotations

from dominio.objetos_de_valor.numero_maior_que_zero import NumeroMaiorQueZero


class NumeroDeModulo:
    __valor: NumeroMaiorQueZero

    def __init__(self, valor: int) -> None:
        self.__valor = NumeroMaiorQueZero(valor=valor, maximo=20)

    @property
    def valor(self) -> int:
        return self.__valor.valor

    def __eq__(self, outro: NumeroDeModulo) -> bool:
        return self.valor == outro.valor
