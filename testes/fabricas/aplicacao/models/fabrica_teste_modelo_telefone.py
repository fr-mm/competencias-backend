import factory

from aplicacao.models import ModeloTelefone
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_docente import FabricaTesteModeloDocente
from testes.fabricas.auxiliares import GerarTelefone


class FabricaTesteModeloTelefone(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloTelefone

    numero = GerarTelefone.gerar()
    docente = factory.SubFactory(FabricaTesteModeloDocente)
