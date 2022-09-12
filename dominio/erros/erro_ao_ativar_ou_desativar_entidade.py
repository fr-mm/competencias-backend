from uuid import UUID

from dominio.erros import ErroDeDominio


class ErroAoAtivarOuDesativarEntidade(ErroDeDominio):
    def __init__(self, nome_do_docente: str, id_do_docente: UUID, tentou_mudar_ativo_para: bool) -> None:
        if tentou_mudar_ativo_para:
            acao = 'ativar'
            estado = 'ativo'
        else:
            acao = 'desativar'
            estado = 'desativado'

        mensagem = f'Impossível {acao} {nome_do_docente} ({id_do_docente}): já estava {estado}'
        super().__init__(mensagem)
