from rest_framework import serializers


class SerializerOTDModulo(serializers.Serializer):
    id = serializers.UUIDField()
    numero = serializers.IntegerField(min_value=1)
    disciplinas_ids = serializers.ListField(
        child=serializers.UUIDField()
    )
