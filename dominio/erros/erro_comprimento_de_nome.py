from dominio.erros.erro_de_dominio import ErroDeDominio


class ErroComprimentoDeNome(ErroDeDominio):
    def __init__(self, nome: str, tamanho_minimo: int, tamanho_maximo: int) -> None:
        mensagem = f'{nome} tem {len(nome)} caracteres. Mínimo: {tamanho_minimo}, máximo: {tamanho_maximo}'
        super().__init__(mensagem)
