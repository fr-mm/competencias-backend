from rest_framework import serializers


class SerializerOTDCurso(serializers.Serializer):
    id = serializers.UUIDField()
    nome = serializers.CharField(max_length=200)
    modulos = serializers.ListField()
    ativo = serializers.BooleanField()
