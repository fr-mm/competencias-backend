from knox.models import AuthToken
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from aplicacao.serializers import SerializerCadastroUsuario, SerializerModeloUsuario


class UsuariosView(GenericAPIView):
    serializer_class = SerializerCadastroUsuario

    def post(self, request: Request) -> Response:
        """
        Cadastra novo usuário
        """
        serializer: SerializerCadastroUsuario = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        modelo_usuario = serializer.save()
        return Response({
            'usuario': SerializerModeloUsuario(modelo_usuario, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(modelo_usuario)[1]
        })
