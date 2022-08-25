from unittest import TestCase

from dominio.objetos_de_valor import NomeDeDocente
from dominio.otds import OTDDocenteEmCriacao
from testes.fabricas import FabricaTesteOTDDocenteEmCriacao


class TestOTDDocenteEmCriacao(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDDocenteEmCriacao = FabricaTesteOTDDocenteEmCriacao.build()

        docente = otd.para_entidade()

        atributos_resultantes = [
            docente.nome
        ]
        atributos_esperados = [
            NomeDeDocente(otd.nome)
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
