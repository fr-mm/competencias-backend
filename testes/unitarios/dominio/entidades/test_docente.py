from unittest import TestCase

from testes.fabricas import FabricaTesteNomeDeDocente, FabricaTesteIdDeDocente
from dominio.entidades import Docente


class TestDocente(TestCase):
    def test_construir_QUANDO_id_informado_ENTAO_atribui_id(self) -> None:
        nome = FabricaTesteNomeDeDocente.build().valor
        id_ = FabricaTesteIdDeDocente.build().valor

        docente = Docente.construir(
            nome=nome,
            id_=id_
        )

        self.assertEqual(docente.id.valor, id_)

    def test_construir_QUANDO_id_nao_informado_ENTAO_atribui_id_gerado_nao_nulo(self) -> None:
        nome = FabricaTesteNomeDeDocente.build().valor

        docente = Docente.construir(
            nome=nome
        )
        self.assertIsNotNone(docente.id.valor)

    def test_construir_QUANDO_ativo_nao_informado_ENTAO_atribui_true(self) -> None:
        nome = FabricaTesteNomeDeDocente.build().valor

        docente = Docente.construir(
            nome=nome
        )
        self.assertTrue(docente.ativo)
