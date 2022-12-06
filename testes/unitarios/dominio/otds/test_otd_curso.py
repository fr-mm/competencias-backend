from unittest import TestCase

from dominio.entidades import Curso
from dominio.objetos_de_valor import Id, NomeDeDisciplina
from dominio.otds import OTDCurso
from testes.fabricas import FabricaTesteOTDCurso, FabricaTesteCurso


class TestOTDCurso(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDCurso = FabricaTesteOTDCurso.build()

        curso = otd.para_entidade()

        atributos_resultantes = [
            curso.id,
            curso.nome,
            curso.modulos_ids,
            curso.ativo
        ]
        atributos_esperados = [
            Id(otd.id),
            NomeDeDisciplina(otd.nome),
            [Id(id_) for id_ in otd.modulos_ids],
            otd.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_de_entidade_QUANDO_entidade_informada_ENTAO_retorna_otd_esperado(self) -> None:
        curso: Curso = FabricaTesteCurso.build()

        otd = OTDCurso.de_entidade(curso)

        otd_esperado = OTDCurso(
            id=curso.id.valor,
            nome=curso.nome.valor,
            modulos_ids=[id_.valor for id_ in curso.modulos_ids],
            ativo=otd.ativo
        )
        self.assertEqual(otd, otd_esperado)
