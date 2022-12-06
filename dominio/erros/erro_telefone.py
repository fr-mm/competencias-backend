from dominio.erros.erro_de_dominio import ErroDeDominio


class ErroTelefone(ErroDeDominio):
    def __init__(self, telefone: str) -> None:
        mensagem = f'Telefone inválido: {telefone}'
        super().__init__(mensagem)
