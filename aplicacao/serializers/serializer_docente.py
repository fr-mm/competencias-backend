from rest_framework import serializers


class SerializerDocente(serializers.Serializer):
    id = serializers.UUIDField()
    nome = serializers.CharField(max_length=200)
