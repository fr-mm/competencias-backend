import factory

from dominio.objetos_de_valor.nome_generico import NomeGenerico


class FabricaTesteNomeGenerico(factory.Factory):
    class Meta:
        model = NomeGenerico

    valor = factory.Faker('name')
    tamanho_minimo = 1
    tamanho_maximo = 200
