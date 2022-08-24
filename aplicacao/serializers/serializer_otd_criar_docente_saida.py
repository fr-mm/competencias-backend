from rest_framework import serializers

from aplicacao.serializers.base import SerializerBaseOTDSaida


class SerializerOTDCriarDocenteSaida(SerializerBaseOTDSaida):
    id = serializers.UUIDField()
    nome = serializers.CharField(max_length=200)
