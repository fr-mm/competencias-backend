from unittest import TestCase

from aplicacao.erros import ErroDeSerializacao
from aplicacao.serializers import SerializerOTDCriarDocenteEntrada
from dominio.otds import OTDEntradaCasoDeUsoCriarDocente
from testes.fabricas.dominio.otds import FabricaTesteOTDEntradaCasoDeUsoCriarDocente


class TestSerializerBaseOTDEntrada(TestCase):
    def setUp(self) -> None:
        self.serializer_class = SerializerOTDCriarDocenteEntrada
        self.otd_entrada_valido: OTDEntradaCasoDeUsoCriarDocente = FabricaTesteOTDEntradaCasoDeUsoCriarDocente.build()
        self.request_data_valido = {
            'nome': self.otd_entrada_valido.nome
        }

    def test_is_valid_QUANDO_request_data_valido_ENTAO_retorna_true(self) -> None:
        serializer = self.serializer_class(data=self.request_data_valido)

        resultado = serializer.is_valid()

        self.assertTrue(resultado)

    def test_is_valid_QUANDO_requeset_data_invalido_ENTAO_retorna_false(self) -> None:
        request_data = {}
        serializer = self.serializer_class(data=request_data)

        resultlado = serializer.is_valid()

        self.assertFalse(resultlado)

    def test_para_otd_QUANDO_valido_ENTAO_retorna_otd_esperado(self) -> None:
        otd_resultante = self.serializer_class.request_data_para_otd(self.request_data_valido)

        self.assertEqual(otd_resultante, self.otd_entrada_valido)

    def test_para_otd_QUANDO_invalido_ENTAO_lanca_erro_de_serializacao(self) -> None:
        request_data = {}

        with self.assertRaises(ErroDeSerializacao):
            self.serializer_class.request_data_para_otd(request_data)
