from rest_framework import serializers

from dominio.otds import OTDDocenteEmCriacao


class SerializerOTDDocenteEmCriacao(serializers.Serializer):
    otd_class = OTDDocenteEmCriacao

    nome = serializers.CharField(max_length=200)
