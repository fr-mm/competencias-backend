from __future__ import annotations

from dominio.erros import ErroNomeMuitoCurto


class NomeDeUsuario:
    __TAMANHO_MINIMO = 3
    __valor: str

    def __init__(self, valor: str) -> None:
        self.__validar(valor)
        self.__valor = valor

    @property
    def valor(self) -> str:
        return self.__valor

    def __eq__(self, nome_de_usuario: NomeDeUsuario) -> bool:
        return self.valor == nome_de_usuario.valor

    def __validar(self, valor: str) -> None:
        self.__validar_tamanho(valor)

    @staticmethod
    def __validar_tamanho(valor: str) -> None:
        if len(valor) < NomeDeUsuario.__TAMANHO_MINIMO:
            raise ErroNomeMuitoCurto(nome=valor, tamanho_minimo=NomeDeUsuario.__TAMANHO_MINIMO)
