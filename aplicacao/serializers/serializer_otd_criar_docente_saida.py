from rest_framework import serializers

from aplicacao.serializers.serializer_abstrato import SerializerAbstrato


class SerializerOTDCriarDocenteSaida(SerializerAbstrato):
    id = serializers.UUIDField()
    nome = serializers.CharField(max_length=200)
