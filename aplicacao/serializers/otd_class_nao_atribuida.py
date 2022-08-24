from aplicacao.erros import ErroSerializerSemOTDAtribuido


class OTDClass:
    def __init__(self, **kwargs) -> None:
        raise ErroSerializerSemOTDAtribuido()
