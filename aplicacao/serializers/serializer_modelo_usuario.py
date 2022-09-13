from rest_framework import serializers

from aplicacao.models import ModeloUsuario


class SerializerModeloUsuario(serializers):
    class Meta:
        model = ModeloUsuario
        fields = ('id', 'username', 'email')
