from dominio.erros.erro_nome_de_docente import ErroNomeDeDocente


class ErroNomeDeDocenteMuitoCurto(ErroNomeDeDocente):
    def __init__(self, nome: str, tamanho_minimo: int) -> None:
        mensagem = f'{nome} só tem {len(nome)} caracteres, tamanho mínimo é {tamanho_minimo}'
        super().__init__(mensagem)
