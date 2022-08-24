from rest_framework.exceptions import ValidationError

from aplicacao.erros import ErroSerializerSemOTDAtribuido, ErroDeSerializacao
from aplicacao.serializers.serializer_base import SerializerBase


class OTDClass:
    def __init__(self, **kwargs) -> None:
        raise ErroSerializerSemOTDAtribuido()


class SerializerBaseOTDEntrada(SerializerBase):
    otd_class = OTDClass

    def para_otd(self) -> otd_class:
        try:
            self.is_valid(raise_exception=True)
            return self.otd_class(**self.validated_data)

        except ValidationError:
            raise ErroDeSerializacao()
