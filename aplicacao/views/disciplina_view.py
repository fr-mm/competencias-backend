from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.serializers import SerializerOTDDisciplina
from dominio.erros import ErroDisciplinaNaoEncontrada
from dominio.otds import OTDDisciplina


class DisciplinaView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias):
        self.__container = container
        super().__init__()

    def post(self, request: Request, id_: UUID) -> Response:
        try:
            serializer_otd_entrada = SerializerOTDDisciplina(data=request.data)
            serializer_otd_entrada.is_valid(raise_exception=True)
            otd_entrada = OTDDisciplina(**serializer_otd_entrada.validated_data)
            otd_saida = self.__container.casos_de_uso.disciplina.editar.executar(otd_entrada)
            serializer_otd_docente_saida = SerializerOTDDisciplina(otd_saida)

            return Response(
                data=serializer_otd_docente_saida.data,
                status=200
            )
        except ErroDisciplinaNaoEncontrada:
            return Response(
                status=404
            )
