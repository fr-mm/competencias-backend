import factory
from factory import fuzzy

from dominio.entidades import Competencia
from dominio.enums import NivelDeCompetenciaEnum
from testes.fabricas.dominio.objetos_de_valor import FabricaTesteId


class FabricaTesteCompetencia(factory.Factory):
    class Meta:
        model = Competencia

    docente_id = factory.SubFactory(FabricaTesteId)
    disciplina_id = factory.SubFactory(FabricaTesteId)
    nivel = fuzzy.FuzzyChoice([nivel for nivel in NivelDeCompetenciaEnum])
