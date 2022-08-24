from aplicacao.serializers.serializer_base import SerializerBase
from dominio.otds import OTDBase


class Foo:
    pass


class SerializerBaseOTDEntrada(SerializerBase):
    otd_class = OTDBase

    def para_otd(self) -> otd_class:
        self.is_valid(raise_exception=True)
        return self.otd_class(**self.validated_data)
