from unittest import TestCase

from dominio.objetos_de_valor import CargaHoraria
from testes.fabricas import FabricaTesteCargaHoraria


class TestCargaHoraria(TestCase):
    def test_valor_QUANDO_valor_atribuido_ENTAO_retorna_valor(self) -> None:
        valor = 2
        carga_horaria: CargaHoraria = FabricaTesteCargaHoraria.build(valor=valor)

        resultado = carga_horaria.valor

        self.assertEqual(resultado, valor)

    def test_eq_QUANDO_valores_iguais_ENTAO_retorna_true(self) -> None:
        carga_horaria1: CargaHoraria = FabricaTesteCargaHoraria.build(valor=2)
        carga_horaria2: CargaHoraria = FabricaTesteCargaHoraria.build(valor=2)

        resultado = carga_horaria1 == carga_horaria2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_diferentes_ENTAO_retorna_false(self) -> None:
        carga_horaria1: CargaHoraria = FabricaTesteCargaHoraria.build(valor=2)
        carga_horaria2: CargaHoraria = FabricaTesteCargaHoraria.build(valor=3)

        resultado = carga_horaria1 == carga_horaria2

        self.assertFalse(resultado)
