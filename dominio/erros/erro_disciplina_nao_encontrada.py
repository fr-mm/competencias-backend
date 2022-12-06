from uuid import UUID

from dominio.erros.erro_de_dominio import ErroDeDominio


class ErroDisciplinaNaoEncontrada(ErroDeDominio):
    def __init__(self, id_: UUID) -> None:
        mensagem = f'Não foi encontrada Disciplina com id {id_}'
        super().__init__(mensagem)
