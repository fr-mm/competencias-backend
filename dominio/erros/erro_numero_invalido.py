from dominio.erros import ErroDeDominio


class ErroNumeroInvalido(ErroDeDominio):
    def __init__(self, numero: int, valor_minimo: int, valor_maximo: int) -> None:
        mensagem = f'{numero} está fora da faixa aceitável. Mínimo: {valor_minimo}, máximo: {valor_maximo}'
        super().__init__(mensagem)
