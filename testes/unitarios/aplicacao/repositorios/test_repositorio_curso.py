from django.test import TestCase

from aplicacao.models import ModeloCurso
from aplicacao.repositorios import RepositorioCurso
from dominio.entidades import Curso
from dominio.erros import ErroCursoNaoEncontrado
from dominio.objetos_de_valor import Id
from testes.fabricas import FabricaTesteCurso, FabricaTesteModeloCurso, FabricaTesteId


class TestRepositorioCurso(TestCase):
    def setUp(self) -> None:
        self.repositorio = RepositorioCurso()

    def test_salvar_QUANDO_curso_sem_modulos_ENTAO_salva_curso_no_banco_de_dados(self) -> None:
        curso: Curso = FabricaTesteCurso.build(modulos=[])

        self.repositorio.salvar(curso)

        ModeloCurso.objects.get(pk=curso.id.valor)

    def test_trazer_por_id_QUANDO_curso_existe_ENTAO_retorna_curso(self) -> None:
        modelo_curso: ModeloCurso = FabricaTesteModeloCurso.create()
        id_ = Id(modelo_curso.id)

        curso = self.repositorio.trazer_por_id(id_)

        self.assertEqual(curso.id, id_)

    def test_trazer_por_id_QUANDO_disciplina_nao_existe_ENTAO_lanca_erro_disciplina_nao_encontrada(self) -> None:
        id_ = FabricaTesteId.build()

        with self.assertRaises(ErroCursoNaoEncontrado):
            self.repositorio.trazer_por_id(id_)
