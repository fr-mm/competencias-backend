from __future__ import annotations

from rest_framework import serializers

from aplicacao.serializers.base import SerializerBaseOTDEntrada
from dominio.otds import OTDEntradaCasoDeUsoCriarDocente


class SerializerOTDCriarDocenteEntrada(SerializerBaseOTDEntrada):
    otd_class = OTDEntradaCasoDeUsoCriarDocente

    nome = serializers.CharField(max_length=200)
