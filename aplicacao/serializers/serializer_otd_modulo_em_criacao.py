from rest_framework import serializers


class SerializerOTDModuloEmCriacao(serializers.Serializer):
    numero = serializers.IntegerField(min_value=1)
    disciplinas_ids = serializers.ListField(
        child=serializers.UUIDField()
    )
