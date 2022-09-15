from typing import Dict

from knox.serializers import UserSerializer as KnoxUserSerializer

from aplicacao.models import ModeloUsuario


class SerializerCadastroUsuario(KnoxUserSerializer):
    class Meta:
        model = ModeloUsuario
        fields = ('id', 'nome', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: Dict[str, str]) -> ModeloUsuario:
        return ModeloUsuario.objects.create_user(
            nome=validated_data['nome'],
            email=validated_data['email'],
            password=validated_data['password']
        )
