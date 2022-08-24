from __future__ import annotations

from rest_framework import serializers

from aplicacao.serializers.serializer_base import SerializerBase
from dominio.otds import OTDEntradaCasoDeUsoCriarDocente


class SerializerOTDCriarDocenteEntrada(SerializerBase):
    otd_class = OTDEntradaCasoDeUsoCriarDocente
    nome = serializers.CharField(max_length=200)

    def para_otd(self) -> otd_class:
        self.is_valid(raise_exception=True)
        return self.otd_class(**self.validated_data)
