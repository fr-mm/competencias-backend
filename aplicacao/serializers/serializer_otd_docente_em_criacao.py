from rest_framework import serializers

from dominio.otds import OTDCriarDocenteEntrada


class SerializerOTDDocenteEmCriacao(serializers.Serializer):
    otd_class = OTDCriarDocenteEntrada

    nome = serializers.CharField(max_length=200)
