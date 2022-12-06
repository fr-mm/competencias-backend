import factory

from dominio.objetos_de_valor import Telefone
from testes.fabricas.auxiliares import GerarTelefone


class FabricaTesteTelefone(factory.Factory):
    class Meta:
        model = Telefone

    valor = GerarTelefone.gerar()
