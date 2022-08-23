from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.serializers import SerializerDocente, SerializerDocenteSemID
from dominio.otds import OTDEntradaCasoDeUsoCriarDocente


class DocentesView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias):
        self.__container = container
        super().__init__()

    def post(self, request: Request) -> Response:
        serializer_entrada = SerializerDocenteSemID(data=request.data)
        try:
            serializer_entrada.is_valid(raise_exception=True)
            otd_entrada_criar_docente = OTDEntradaCasoDeUsoCriarDocente(**serializer_entrada.validated_data)
            otd_saida_criar_docente = self.__container.casos_de_uso.criar_docente.executar(otd_entrada_criar_docente)
            serializer_saida = SerializerDocente(otd_saida_criar_docente)

            return Response(
                data=serializer_saida.data,
                status=201,
                content_type='json'
            )
        except ValidationError:
            return Response(status=400)
