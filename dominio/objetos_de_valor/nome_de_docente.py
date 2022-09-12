from __future__ import annotations

from dominio.erros import ErroNomeMuitoCurto


class NomeDeDocente:
    __TAMANHO_MINIMO = 3
    __valor: str

    def __init__(self, valor: str) -> None:
        self.__validar(valor)
        self.__valor = valor

    @property
    def valor(self) -> str:
        return self.__valor

    def __eq__(self, nome_de_docente: NomeDeDocente) -> bool:
        return self.valor == nome_de_docente.valor

    def __validar(self, valor: str) -> None:
        self.__validar_tamanho(valor)

    @staticmethod
    def __validar_tamanho(valor: str) -> None:
        if len(valor) < NomeDeDocente.__TAMANHO_MINIMO:
            raise ErroNomeMuitoCurto(nome=valor, tamanho_minimo=NomeDeDocente.__TAMANHO_MINIMO)
