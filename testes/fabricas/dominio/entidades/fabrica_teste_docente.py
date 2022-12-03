import factory

from testes.fabricas.dominio.objetos_de_valor import FabricaTesteNomeDeDocente, FabricaTesteId
from dominio.entidades import Docente


class FabricaTesteDocente(factory.Factory):
    class Meta:
        model = Docente

    nome = factory.SubFactory(FabricaTesteNomeDeDocente)
    id_ = factory.SubFactory(FabricaTesteId)
    ativo = factory.Faker('boolean')
