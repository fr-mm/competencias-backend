from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicacao.container import ContainerDeDependencias, container_de_dependencias
from aplicacao.models import ModeloDisciplina
from aplicacao.serializers import SerializerOTDCasoDeUsoEditarCompetencias, SerializerOTDCompetencia
from dominio.otds import OTDCasoDeUsoEditarCompetencias, OTDCompetencia


class CompetenciasView(APIView):
    __container: ContainerDeDependencias

    def __init__(self, container: ContainerDeDependencias = container_de_dependencias):
        self.__container = container
        super().__init__()

    def post(self, request: Request) -> Response:
        try:
            serializer = SerializerOTDCasoDeUsoEditarCompetencias(data=request.data)
            serializer.is_valid(raise_exception=True)
            otd = OTDCasoDeUsoEditarCompetencias(**serializer.validated_data)
            competencias = []
            for competencia in otd.competencias:
                serializer_competencia = SerializerOTDCompetencia(data=competencia)
                serializer_competencia.is_valid(raise_exception=True)
                otd_competencia = OTDCompetencia(**serializer_competencia.validated_data)
                competencias.append(otd_competencia)
            otd.competencias = competencias
            self.__container.casos_de_uso.competencia.editar.executar(otd)

            return Response(status=200)

        except ValidationError:
            return Response(status=400)
