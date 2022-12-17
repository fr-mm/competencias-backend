from rest_framework import serializers


class SerializerOTDCompetencia(serializers.Serializer):
    docente_id = serializers.UUIDField()
    disciplina_id = serializers.UUIDField()
    nivel = serializers.IntegerField()

