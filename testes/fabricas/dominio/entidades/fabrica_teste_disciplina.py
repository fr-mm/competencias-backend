import factory

from dominio.entidades import Disciplina
from testes.fabricas.dominio.objetos_de_valor.fabrica_teste_id import FabricaTesteId
from testes.fabricas.dominio.objetos_de_valor.fabrica_teste_nome_de_disciplina import FabricaTesteNomeDeDisciplina
from testes.fabricas.dominio.objetos_de_valor.fabrica_teste_carga_horaria import FabricaTesteCargaHoraria


class FabricaTesteDisciplina(factory.Factory):
    class Meta:
        model = Disciplina

    id_ = factory.SubFactory(FabricaTesteId)
    nome = factory.SubFactory(FabricaTesteNomeDeDisciplina)
    carga_horaria = factory.SubFactory(FabricaTesteCargaHoraria)
    ativo = factory.Faker('pybool')
