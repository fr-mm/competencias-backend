from __future__ import annotations

from dataclasses import dataclass

from dominio.erros import ErroComprimentoDeNome


@dataclass(frozen=True)
class NomeGenerico:
    tamanho_minimo: int
    tamanho_maximo: int
    valor: str

    def __post_init__(self) -> None:
        self.__validar_tamanho()

    def __validar_tamanho(self) -> None:
        tamanho = len(self.valor)
        if tamanho < self.tamanho_minimo or tamanho > self.tamanho_maximo:
            raise ErroComprimentoDeNome(
                nome=self.valor,
                tamanho_minimo=self.tamanho_minimo,
                tamanho_maximo=self.tamanho_maximo
            )

    def __eq__(self, outro: NomeGenerico) -> bool:
        return self.valor == outro.valor
