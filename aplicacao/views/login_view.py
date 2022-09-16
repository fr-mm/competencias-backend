from knox.models import AuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.serializers import SerializerLogin, SerializerModeloUsuario


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        """
        Faz o login de um usuário no sistema
        """
        try:
            serializer = SerializerLogin(data=request.data)
            serializer.is_valid(raise_exception=True)
            usuario = serializer.validated_data
            return Response(
                data={
                    'usuario': SerializerModeloUsuario(usuario, context=serializer.context).data,
                    'token': AuthToken.objects.create(usuario)[1]
                },
                status=200
            )

        except ValidationError:
            return Response(status=400)
