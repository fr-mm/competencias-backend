import factory

from testes.fabricas.dominio.objetos_de_valor import FabricaTesteNomeDeDocente, FabricaTesteIdDeDocente
from dominio.entidades import Docente


class FabricaTesteDocente(factory.Factory):
    class Meta:
        model = Docente

    nome = factory.SubFactory(FabricaTesteNomeDeDocente)
    id = factory.SubFactory(FabricaTesteIdDeDocente)
