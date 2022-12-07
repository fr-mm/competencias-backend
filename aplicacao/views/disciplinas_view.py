from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.serializers import SerializerOTDDisciplinaEmCriacao, SerializerOTDDisciplina
from dominio.otds import OTDDisciplinaEmCriacao


class DisciplinasView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias) -> None:
        self.__container = container
        super().__init__()

    def post(self, request: Request) -> Response:
        try:
            serializer_otd_disciplina_em_criacao = SerializerOTDDisciplinaEmCriacao(data=request.data)
            serializer_otd_disciplina_em_criacao.is_valid(raise_exception=True)
            otd_disciplina_em_criacao = OTDDisciplinaEmCriacao(**serializer_otd_disciplina_em_criacao.validated_data)
            otd_disciplina = self.__container.casos_de_uso.disciplina.criar.executar(otd_disciplina_em_criacao)
            serializer_otd_disciplina = SerializerOTDDisciplina(otd_disciplina)

            return Response(
                data=serializer_otd_disciplina.data,
                status=201
            )
        except ValidationError:
            return Response(status=400)
