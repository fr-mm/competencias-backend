from rest_framework import serializers


class SerializerOTDCursoEmCriacao(serializers.Serializer):
    nome = serializers.CharField(max_length=200)
    modulos = serializers.ListField()
