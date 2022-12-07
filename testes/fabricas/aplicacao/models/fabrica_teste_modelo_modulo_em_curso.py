import factory.django

from aplicacao.models import ModeloModuloEmCurso
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_curso import FabricaTesteModeloCurso
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_modulo import FabricaTesteModeloModulo


class FabricaTesteModeloModuloEmCurso(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloModuloEmCurso

    curso = factory.SubFactory(FabricaTesteModeloCurso)
    modulo = factory.SubFactory(FabricaTesteModeloModulo)
