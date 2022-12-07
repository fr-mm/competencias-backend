from rest_framework import serializers


class SerializerOTDDisciplina(serializers.Serializer):
    id = serializers.UUIDField()
    nome = serializers.CharField(max_length=200)
    carga_horaria = serializers.IntegerField()
    ativo = serializers.BooleanField()
