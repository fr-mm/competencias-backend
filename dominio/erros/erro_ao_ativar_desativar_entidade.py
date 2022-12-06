from uuid import UUID

from dominio.erros.erro_de_dominio import ErroDeDominio


class ErroAoAtivarDesativarEntidade(ErroDeDominio):
    def __init__(self, nome_da_entidade: str, id_da_entidade: UUID, tentou_mudar_ativo_para: bool) -> None:
        if tentou_mudar_ativo_para:
            acao = 'ativar'
            estado = 'ativo'
        else:
            acao = 'desativar'
            estado = 'desativado'

        mensagem = f'Impossível {acao} {nome_da_entidade} (id:{id_da_entidade}): já estava {estado}'
        super().__init__(mensagem)
