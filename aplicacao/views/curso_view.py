from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.serializers import SerializerOTDCurso
from dominio.erros import ErroCursoNaoEncontrado
from dominio.otds import OTDCurso


class CursoView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias):
        self.__container = container
        super().__init__()

    def post(self, request: Request, id_: UUID) -> Response:
        try:
            serializer_entrada = SerializerOTDCurso(data=request.data)
            serializer_entrada.is_valid(raise_exception=True)
            otd_entrada = OTDCurso(**serializer_entrada.validated_data)
            otd_saida = self.__container.casos_de_uso.curso.editar.executar(otd_entrada)
            serializer_saida = SerializerOTDCurso(otd_saida)

            return Response(
                data=serializer_saida.data,
                status=200
            )
        except ErroCursoNaoEncontrado:
            return Response(
                status=404
            )
