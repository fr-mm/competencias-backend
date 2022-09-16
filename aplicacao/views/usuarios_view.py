from knox.models import AuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.serializers import SerializerCadastroUsuario, SerializerModeloUsuario


class UsuariosView(APIView):
    def post(self, request: Request) -> Response:
        """
        Cadastra novo usuário
        """
        try:
            serializer: SerializerCadastroUsuario = SerializerCadastroUsuario(data=request.data)
            serializer.is_valid(raise_exception=True)
            modelo_usuario = serializer.save()
            token = AuthToken.objects.create(modelo_usuario)
            return Response(
                data={
                    'usuario': SerializerModeloUsuario(modelo_usuario, context=serializer.context).data,
                    'token': token[1]
                },
                status=201
            )
        except ValidationError:
            return Response(status=400)
