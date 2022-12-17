from rest_framework import serializers


class SerializerOTDCasoDeUsoEditarCompetencias(serializers.Serializer):
    docente_id = serializers.UUIDField()
    competencias = serializers.ListField()
