from rest_framework import serializers


class SerializerOTDCurso(serializers.Serializer):
    id = serializers.UUIDField()
    nome = serializers.CharField(max_length=200)
    modulos_ids = serializers.ListField(
        child=serializers.UUIDField()
    )
    ativo = serializers.BooleanField()
