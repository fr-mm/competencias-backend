from uuid import UUID

from dominio.erros.erro_de_dominio import ErroDeDominio


class ErroDocenteNaoEncontrado(ErroDeDominio):
    def __init__(self, id_: UUID) -> None:
        mensagem = f'Não foi encontrado Docente com id {id_}'
        super().__init__(mensagem)
