from __future__ import annotations

from rest_framework import serializers

from aplicacao.serializers.serializer_abstrato import SerializerAbstrato


class SerializerOTDCriarDocenteEntrada(SerializerAbstrato):
    nome = serializers.CharField(max_length=200)
