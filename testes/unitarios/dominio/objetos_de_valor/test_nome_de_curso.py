from unittest import TestCase

from dominio.objetos_de_valor import NomeDeCurso
from testes.fabricas import FabricaTesteNomeDeCurso


class TestNomeDeCurso(TestCase):
    def test_valor_QUANDO_chamado_ENTAO_retorna_valor(self) -> None:
        valor = 'Foobar'
        nome_de_curso = NomeDeCurso(valor)

        resultado = nome_de_curso.valor

        self.assertEqual(resultado, valor)

    def test_eq_QUANDO_iguais_ENTAO_retorna_true(self) -> None:
        nome_de_curso1: NomeDeCurso = FabricaTesteNomeDeCurso.build()
        nome_de_curso2: NomeDeCurso = FabricaTesteNomeDeCurso.build(valor=nome_de_curso1.valor)

        resultado = nome_de_curso1 == nome_de_curso2

        self.assertTrue(resultado)

    def test_eq_QUANDO_diferentes_ENTAO_retorna_false(self) -> None:
        nome_de_curso1 = NomeDeCurso('Foobar')
        nome_de_curso2 = NomeDeCurso('Barfoo')

        resultado = nome_de_curso1 == nome_de_curso2

        self.assertFalse(resultado)
