from dominio.erros.erro_de_dominio import ErroDeDominio


class ErroEmail(ErroDeDominio):
    def __init__(self, email: str) -> None:
        mensagem = f'Email inválido: {email}'
        super().__init__(mensagem)
