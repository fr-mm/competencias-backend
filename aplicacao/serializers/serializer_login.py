from collections import OrderedDict

from django.contrib.auth import authenticate
from rest_framework import serializers

from aplicacao.models import ModeloUsuario


class SerializerLogin(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, dados: OrderedDict) -> ModeloUsuario:
        print('ieauheauihouieahiueahiuheauheiauhieua')
        usuario = authenticate(**dados)
        if usuario and usuario.is_active:
            print(type(usuario))
            return usuario
        raise serializers.ValidationError('Credenciais inválidas')
