from unittest import TestCase

from dominio.entidades import Docente
from dominio.objetos_de_valor import IdDeDocente, NomeDeDocente
from testes.fabricas.entidades import FabricaTesteDocente
from testes.fabricas.objetos_de_valor import FabricaTesteIdDeDocente, FabricaTesteNomeDeDocente


class TestDocente(TestCase):
    def test_init_QUANDO_id_informado_ENTAO_atribui_id(self) -> None:
        id_de_docente: IdDeDocente = FabricaTesteIdDeDocente.build()

        docente: Docente = FabricaTesteDocente.build(id=id_de_docente)

        self.assertEqual(docente.id, id_de_docente)

    def test_init_QUANDO_id_nao_informado_ENTAO_atribui_id_gerado(self) -> None:
        nome_de_docente: NomeDeDocente = FabricaTesteNomeDeDocente.build()

        docente = Docente(nome=nome_de_docente)

        self.assertIsInstance(docente.id, IdDeDocente)
