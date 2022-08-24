from typing import Any

from aplicacao.serializers.base.serializer_base import SerializerBase


class SerializerBaseOTDSaida(SerializerBase):
    @classmethod
    def otd_para_response_data(cls, otd: Any) -> Any:
        serializer = cls(otd)
        return serializer.data
