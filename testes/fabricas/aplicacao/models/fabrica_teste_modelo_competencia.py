import factory

from aplicacao.models import ModeloCompetencia
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_docente import FabricaTesteModeloDocente
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_disciplina import FabricaTesteModeloDisciplina


class FabricaTesteModeloCompetencia(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloCompetencia

    docente = factory.SubFactory(FabricaTesteModeloDocente)
    disciplina = factory.SubFactory(FabricaTesteModeloDisciplina)
    nivel = factory.Faker('pyint', min_value=2, max_value=4)
