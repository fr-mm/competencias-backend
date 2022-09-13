from django.contrib.auth import authenticate
from rest_framework import serializers


class SerializerCadastroUsuario(serializers):
    username = serializers.CharField()
    password = serializers.CharField()

    # TODO: tipar
    def validate(self, dados):
        usuario = authenticate(**dados)
        if usuario and usuario.ativo:
            return usuario
        return serializers.ValidationError('Credenciais inválidas')
