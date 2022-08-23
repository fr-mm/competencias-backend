from rest_framework import serializers


class SerializerDocenteSemID(serializers.Serializer):
    nome = serializers.CharField(max_length=200)
