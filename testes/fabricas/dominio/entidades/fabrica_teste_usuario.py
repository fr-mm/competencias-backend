import factory

from dominio.entidades import Usuario
from testes.fabricas.dominio.objetos_de_valor import FabricaTesteIdDeUsuario, FabricaTesteNomeDeUsuario, FabricaTesteEmail


class FabricaTesteUsuario(factory.Factory):
    class Meta:
        model = Usuario

    id_ = factory.SubFactory(FabricaTesteIdDeUsuario)
    nome = factory.SubFactory(FabricaTesteNomeDeUsuario)
    email = factory.SubFactory(FabricaTesteEmail)
    ativo = factory.Faker('bool')
