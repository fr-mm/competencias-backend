from aplicacao.erros.erro_de_aplicacao import ErroDeAplicacao
from dominio.objetos_de_valor import IdDeDocente


class ErroDocenteNaoEncontrado(ErroDeAplicacao):
    def __init__(self, id_do_docente: IdDeDocente) -> None:
        mensagem = f'Não foi encontrado Docente com id {str(id_do_docente.valor)}'
        super().__init__(mensagem)
