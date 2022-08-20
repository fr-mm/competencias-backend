import factory

from dominio.entidades import Docente
from testes.fabricas.dominio.objetos_de_valor import FabricaTesteNomeDeDocente, FabricaTesteIdDeDocente


class FabricaTesteDocente(factory.Factory):
    class Meta:
        model = Docente

    nome = factory.SubFactory(FabricaTesteNomeDeDocente)
    id = factory.SubFactory(FabricaTesteIdDeDocente)
