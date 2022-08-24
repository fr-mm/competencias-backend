from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.erros import ErroDeSerializacao
from aplicacao.serializers import SerializerOTDCriarDocenteEntrada, SerializerOTDCriarDocenteSaida


class DocentesView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias):
        self.__container = container
        super().__init__()

    def post(self, request: Request) -> Response:
        try:
            otd_entrada_criar_docente = SerializerOTDCriarDocenteEntrada.request_data_para_otd(request.data)
            otd_saida_criar_docente = self.__container.casos_de_uso.criar_docente.executar(otd_entrada_criar_docente)
            serializer_saida = SerializerOTDCriarDocenteSaida(otd_saida_criar_docente)

            return Response(
                data=serializer_saida.data,
                status=201,
                content_type='json'
            )
        except ErroDeSerializacao:
            return Response(status=400)
