from django.contrib.auth import authenticate
from knox.serializers import UserSerializer as KnoxUserSerializer
from rest_framework import serializers

from aplicacao.models import ModeloUsuario


class SerializerLogin(KnoxUserSerializer):
    class Meta:
        model = ModeloUsuario
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # TODO: tipar
    def validate(self, dados):
        usuario = authenticate(**dados)
        if usuario and usuario.ativo:
            return usuario
        return serializers.ValidationError('Credenciais inválidas')
