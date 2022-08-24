from typing import Dict

from rest_framework.exceptions import ValidationError

from aplicacao.erros import ErroDeSerializacao
from aplicacao.serializers.base.otd_class_nao_atribuida import OTDClass
from aplicacao.serializers.base.serializer_base import SerializerBase


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
