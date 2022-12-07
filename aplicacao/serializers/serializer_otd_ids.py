from rest_framework import serializers


class SerializerOTDIds(serializers.Serializer):
    ids = serializers.ListField(
        child=serializers.UUIDField()
    )
