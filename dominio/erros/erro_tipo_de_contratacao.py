from dominio.erros.erro_de_dominio import ErroDeDominio


class ErroTipoDeContratacao(ErroDeDominio):
    def __init__(self, tipo_de_contratacao: str) -> None:
        mensagem = f'Tipo de contratação inválido: {tipo_de_contratacao}'
        super().__init__(mensagem)
