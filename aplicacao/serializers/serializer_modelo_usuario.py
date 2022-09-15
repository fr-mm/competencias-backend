from knox.serializers import UserSerializer as KnoxUserSerializer

from aplicacao.models import ModeloUsuario


class SerializerModeloUsuario(KnoxUserSerializer):
    class Meta:
        model = ModeloUsuario
        fields = ('id', 'nome', 'email')
