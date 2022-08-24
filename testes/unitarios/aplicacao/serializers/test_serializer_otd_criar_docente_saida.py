from unittest import TestCase

from aplicacao.serializers import SerializerOTDCriarDocenteSaida
from dominio.otds import OTDSaidaCasoDeUsoCriarDocente
from testes.fabricas.dominio.otds import FabricaTesteOTDSaidaCasoDeUsoCriarDocente


class TestSerializerOTDCriarDocenteSaida(TestCase):
    def test_data_QUANDO_otd_informado_ENTAO_retorna_dict_esperado(self) -> None:
        otd: OTDSaidaCasoDeUsoCriarDocente = FabricaTesteOTDSaidaCasoDeUsoCriarDocente.build()
        serializer = SerializerOTDCriarDocenteSaida(otd)

        resultado = serializer.data

        esperado = {
            'id': otd.id,
            'nome': otd.nome
        }
        self.assertEqual(resultado, esperado)
