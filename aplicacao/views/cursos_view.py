from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.serializers import SerializerOTDCurso, SerializerOTDModuloEmCriacao, SerializerOTDModulo, \
    SerializerOTDCursoEmCriacao
from dominio.otds import OTDModuloEmCriacao, OTDCursoEmCriacao


class CursosView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias):
        self.__container = container
        super().__init__()

    def post(self, request: Request) -> Response:
        try:
            otds_modulos = []
            for modulo in request.data['modulos']:
                serializer_modulo_entrada = SerializerOTDModuloEmCriacao(data=modulo)
                serializer_modulo_entrada.is_valid(raise_exception=True)
                otd = OTDModuloEmCriacao(**serializer_modulo_entrada.validated_data)
                otds_modulos.append(otd)
            data = request.data
            data['modulos'] = otds_modulos
            serializer_entrada = SerializerOTDCursoEmCriacao(data=data)
            serializer_entrada.is_valid(raise_exception=True)
            otd_entrada = OTDCursoEmCriacao(**serializer_entrada.validated_data)
            otd_saida = self.__container.casos_de_uso.curso.criar.executar(otd_entrada)
            modulos = []
            for modulo in otd_saida.modulos:
                serializer_modulo_saida = SerializerOTDModulo(data=modulo)
                serializer_modulo_saida.is_valid(raise_exception=True)
                modulos.append(serializer_modulo_saida.validated_data)
            otd_saida.modulos = modulos
            serializer_saida = SerializerOTDCurso(otd_saida)

            return Response(
                data=serializer_saida.data,
                status=201
            )
        except ValidationError:
            return Response(status=400)
