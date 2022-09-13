from rest_framework import serializers

from aplicacao.models import ModeloUsuario


class SerializerCadastroUsuario(serializers):
    class Meta:
        model = ModeloUsuario
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
