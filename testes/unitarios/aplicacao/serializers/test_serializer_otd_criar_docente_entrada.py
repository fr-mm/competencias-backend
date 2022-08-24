from unittest import TestCase

from aplicacao.serializers import SerializerOTDCriarDocenteEntrada
from dominio.otds import OTDEntradaCasoDeUsoCriarDocente
from testes.fabricas.dominio.otds import FabricaTesteOTDEntradaCasoDeUsoCriarDocente


class TestSerializerOTDCriarDocenteEntrada(TestCase):
    def test_is_valid_QUANDO_request_data_valido_ENTAO_retorna_true(self) -> None:
        otd_entrada_esperado: OTDEntradaCasoDeUsoCriarDocente = FabricaTesteOTDEntradaCasoDeUsoCriarDocente.build()
        request_data = {
            'nome': otd_entrada_esperado.nome
        }
        serializer = SerializerOTDCriarDocenteEntrada(data=request_data)

        resultado = serializer.is_valid()

        self.assertTrue(resultado)

    def test_is_valid_QUANDO_requeset_data_invalido_ENTAO_retorna_false(self) -> None:
        request_data = {}
        serializer = SerializerOTDCriarDocenteEntrada(data=request_data)

        resultlado = serializer.is_valid()

        self.assertFalse(resultlado)
