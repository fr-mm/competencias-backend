import factory.django

from aplicacao.models import ModeloDisciplinaEmModulo
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_disciplina import FabricaTesteModeloDisciplina
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_modulo import FabricaTesteModeloModulo


class FabricaTesteModeloDisciplinaEmModulo(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloDisciplinaEmModulo

    modulo = factory.SubFactory(FabricaTesteModeloModulo)
    disciplina = factory.SubFactory(FabricaTesteModeloDisciplina)
