from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.serializers import SerializerOTDDocente
from dominio.erros import ErroDocenteNaoEncontrado
from dominio.otds import OTDDocente


class DocenteView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias):
        self.__container = container
        super().__init__()

    def get(self, _: Request, id_: UUID) -> Response:
        try:
            otd_docente = self.__container.casos_de_uso.docente.trazer.executar(id_)
            serializer_otd_docente = SerializerOTDDocente(otd_docente)

            return Response(
                data=serializer_otd_docente.data,
                status=200
            )
        except ErroDocenteNaoEncontrado:
            return Response(
                status=404
            )

    def post(self, request: Request, id_: UUID) -> Response:
        try:
            serializer_otd_docente_entrada = SerializerOTDDocente(data=request.data)
            serializer_otd_docente_entrada.is_valid(raise_exception=True)
            otd_docente_entrada = OTDDocente(**serializer_otd_docente_entrada.validated_data)
            otd_docente_saida = self.__container.casos_de_uso.docente.editar.executar(otd_docente_entrada)
            serializer_otd_docente_saida = SerializerOTDDocente(otd_docente_saida)

            return Response(
                data=serializer_otd_docente_saida.data,
                status=200
            )
        except ErroDocenteNaoEncontrado:
            return Response(
                status=404
            )

    def delete(self, _: Request, id_: UUID) -> Response:
        try:
            self.__container.casos_de_uso.docente.desativar.executar(id_)
            return Response(
                status=200
            )
        except ErroDocenteNaoEncontrado:
            return Response(
                status=404
            )
