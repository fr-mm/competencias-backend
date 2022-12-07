from uuid import UUID

from dominio.erros.erro_de_dominio import ErroDeDominio


class ErroCursoNaoEncontrado(ErroDeDominio):
    def __init__(self, id_: UUID) -> None:
        mensagem = f'Não foi encontrado Curso com id {id_}'
        super().__init__(mensagem)
