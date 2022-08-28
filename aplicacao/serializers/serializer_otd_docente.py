from rest_framework import serializers


class SerializerOTDDocente(serializers.Serializer):
    id = serializers.UUIDField()
    nome = serializers.CharField(max_length=200)
    ativo = serializers.BooleanField()
