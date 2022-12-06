from rest_framework import serializers

from dominio.otds import OTDDocenteEmCriacao


class SerializerOTDDocenteEmCriacao(serializers.Serializer):
    otd_class = OTDDocenteEmCriacao

    nome = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    telefones = serializers.ListField(
        child=serializers.CharField(max_length=14)
    )
    tipo_de_contratacao = serializers.CharField(max_length=200)
    unidade_senai_id = serializers.CharField(max_length=200)
