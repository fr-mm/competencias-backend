from typing import Dict

from rest_framework.exceptions import ValidationError

from aplicacao.erros import ErroSerializerSemOTDAtribuido, ErroDeSerializacao
from aplicacao.serializers.serializer_base import SerializerBase


class OTDClass:
    def __init__(self, **kwargs) -> None:
        raise ErroSerializerSemOTDAtribuido()


class SerializerBaseOTDEntrada(SerializerBase):
    otd_class = OTDClass

    @classmethod
    def request_data_para_otd(cls, request_data: Dict) -> otd_class:
        serializer = cls(data=request_data)

        try:
            serializer.is_valid(raise_exception=True)
            return serializer.otd_class(**serializer.validated_data)

        except ValidationError:
            raise ErroDeSerializacao()
