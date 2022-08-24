from rest_framework import serializers

from aplicacao.serializers.serializer_base_otd_saida import SerializerBaseOTDSaida


class SerializerOTDCriarDocenteSaida(SerializerBaseOTDSaida):
    id = serializers.UUIDField()
    nome = serializers.CharField(max_length=200)
