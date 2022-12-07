from rest_framework import serializers


class SerializerOTDDisciplinaEmCriacao(serializers.Serializer):
    nome = serializers.CharField(max_length=200)
    carga_horaria = serializers.IntegerField()
