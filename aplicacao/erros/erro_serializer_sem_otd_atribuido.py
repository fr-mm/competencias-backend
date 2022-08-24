from aplicacao.erros.erro_de_aplicacao import ErroDeAplicacao


class ErroSerializerSemOTDAtribuido(ErroDeAplicacao):
    def __init__(self) -> None:
        mensagem = f'Um serializer não possui atributo otd_class sobrescrito'
        super().__init__(mensagem)
