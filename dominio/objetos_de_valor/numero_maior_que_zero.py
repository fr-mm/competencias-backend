from __future__ import annotations

from dataclasses import dataclass

from dominio.erros import ErroNumeroInvalido


@dataclass
class NumeroMaiorQueZero:
    valor: int
    maximo: int

    def __post_init__(self) -> None:
        if self.valor < 1 or self.valor > self.maximo:
            raise ErroNumeroInvalido(
                numero=self.valor,
                valor_minimo=1,
                valor_maximo=self.maximo
            )

    def __eq__(self, outro: NumeroMaiorQueZero):
        return self.valor == outro.valor
