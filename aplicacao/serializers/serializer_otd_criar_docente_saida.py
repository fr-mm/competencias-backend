from rest_framework import serializers

from aplicacao.serializers.serializer_base import SerializerBase


class SerializerOTDCriarDocenteSaida(SerializerBase):
    id = serializers.UUIDField()
    nome = serializers.CharField(max_length=200)
