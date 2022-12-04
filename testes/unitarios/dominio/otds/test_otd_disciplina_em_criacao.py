from unittest import TestCase

from dominio.objetos_de_valor import CargaHoraria, NomeDeDisciplina
from dominio.otds import OTDDisciplinaEmCriacao
from testes.fabricas import FabricaTesteOTDDisciplinaEmCriacao


class TestOTDDisciplinaEmCriacao(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDDisciplinaEmCriacao = FabricaTesteOTDDisciplinaEmCriacao.build()

        disciplina = otd.para_entidade()

        atributos_resultantes = [
            disciplina.nome,
            disciplina.carga_horaria,
            disciplina.ativo
        ]
        atributos_esperados = [
            NomeDeDisciplina(otd.nome),
            CargaHoraria(otd.carga_horaria),
            otd.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
