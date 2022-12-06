from unittest import TestCase

from dominio.entidades import Disciplina
from dominio.objetos_de_valor import Id, CargaHoraria, NomeDeDisciplina
from dominio.otds import OTDDisciplina
from testes.fabricas import FabricaTesteOTDDisciplina, \
    FabricaTesteDisciplina


class TestOTDDisciplina(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDDisciplina = FabricaTesteOTDDisciplina.build()

        disciplina = otd.para_entidade()

        atributos_resultantes = [
            disciplina.id,
            disciplina.nome,
            disciplina.carga_horaria,
            disciplina.ativo
        ]
        atributos_esperados = [
            Id(otd.id),
            NomeDeDisciplina(otd.nome),
            CargaHoraria(otd.carga_horaria),
            otd.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_de_entidade_QUANDO_entidade_informada_ENTAO_retorna_otd_esperado(self) -> None:
        disciplina: Disciplina = FabricaTesteDisciplina.build()

        otd = OTDDisciplina.de_entidade(disciplina)

        otd_esperado = OTDDisciplina(
            id=disciplina.id.valor,
            nome=disciplina.nome.valor,
            carga_horaria=disciplina.carga_horaria.valor,
            ativo=otd.ativo
        )
        self.assertEqual(otd, otd_esperado)
