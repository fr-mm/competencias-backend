from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.serializers import SerializerOTDDocente
from dominio.erros import ErroDocenteNaoEncontrado


class DocenteView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias):
        self.__container = container
        super().__init__()

    def get(self, _: Request, id_: UUID) -> Response:
        try:
            otds_docente = self.__container.casos_de_uso.trazer_docente.executar(id_)
            serializer_otd_docente = SerializerOTDDocente(otds_docente)

            return Response(
                data=serializer_otd_docente.data,
                status=200,
                content_type='json'
            )
        except ErroDocenteNaoEncontrado:
            return Response(
                status=404
            )
