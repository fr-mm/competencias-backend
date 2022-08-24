from aplicacao.serializers.serializer_base import SerializerBase


class OTDClassNaoAtribuido:
    def __init__(self, **kwargs) -> None:
        raise Exception('Classe de OTD não atribuída no serializer')


class SerializerBaseOTDEntrada(SerializerBase):
    otd_class = OTDClassNaoAtribuido

    def para_otd(self) -> otd_class:
        self.is_valid(raise_exception=True)
        return self.otd_class(**self.validated_data)
