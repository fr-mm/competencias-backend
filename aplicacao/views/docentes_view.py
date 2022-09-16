from knox.auth import TokenAuthentication
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.serializers import SerializerOTDDocenteEmCriacao, SerializerOTDDocente
from dominio.otds import OTDDocenteEmCriacao


class DocentesView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias):
        self.__container = container
        super().__init__()

    def post(self, request: Request) -> Response:
        try:
            serializer_otd_docente_em_criacao = SerializerOTDDocenteEmCriacao(data=request.data)
            serializer_otd_docente_em_criacao.is_valid(raise_exception=True)
            otd_docente_em_criacao = OTDDocenteEmCriacao(**serializer_otd_docente_em_criacao.validated_data)
            otd_docente = self.__container.casos_de_uso.criar_docente.executar(otd_docente_em_criacao)
            serializer_otd_docente = SerializerOTDDocente(otd_docente)

            return Response(
                data=serializer_otd_docente.data,
                status=201
            )
        except ValidationError:
            return Response(status=400)

    def get(self, _: Request) -> Response:
        otds_docente = self.__container.casos_de_uso.filtrar_docentes.executar(ativo=True)
        serializer_otd_docente = SerializerOTDDocente(otds_docente, many=True)

        return Response(
            data=serializer_otd_docente.data,
            status=200
        )
