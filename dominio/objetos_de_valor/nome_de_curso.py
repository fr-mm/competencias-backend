from __future__ import annotations

from dominio.objetos_de_valor.nome_generico import NomeGenerico


class NomeDeCurso:
    __valor: NomeGenerico

    def __init__(self, valor: str) -> None:
        self.__valor = NomeGenerico(valor=valor, tamanho_minimo=3, tamanho_maximo=200)

    @property
    def valor(self) -> str:
        return self.__valor.valor

    def __eq__(self, outro: NomeDeCurso) -> bool:
        return self.valor == outro.valor
