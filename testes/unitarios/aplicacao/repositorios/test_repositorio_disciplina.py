import pytest
from django.test import TestCase

from aplicacao.models import ModeloDisciplina
from aplicacao.repositorios import RepositorioDisciplina
from dominio.erros import ErroDisciplinaNaoEncontrada
from dominio.objetos_de_valor import Id
from testes.fabricas import FabricaTesteModeloDisciplina, FabricaTesteDisciplina, FabricaTesteId


@pytest.mark.django_db
class TestRepositorioDisciplina(TestCase):
    def setUp(self) -> None:
        self.repositorio = RepositorioDisciplina()

    def test_filtrar_QUANDO_nenhum_filtro_informado_ENTAO_retorna_todas_as_disciplinas(self) -> None:
        quantidade = 2
        [FabricaTesteModeloDisciplina.create() for _ in range(quantidade)]

        disciplinas = self.repositorio.filtrar()

        self.assertEqual(len(disciplinas), quantidade)

    def test_filtrar_QUANDO_filtrar_por_ativo_true_ENTAO_retorna_disciplinas_ativas(self) -> None:
        modelos_ativos: [ModeloDisciplina] = [FabricaTesteModeloDisciplina.create(ativo=True) for _ in range(2)]
        [FabricaTesteModeloDisciplina.create(ativo=False) for _ in range(2)]

        disciplinas = self.repositorio.filtrar(ativo=True)

        ids_resultantes = [disciplina.id.valor for disciplina in disciplinas]
        ids_esperados = [modelo.id for modelo in modelos_ativos]
        self.assertEqual(ids_resultantes, ids_esperados)

    def test_salvar_QUANDO_disciplina_informada_ENTAO_salva_disciplina(self) -> None:
        disciplina = FabricaTesteDisciplina.build()

        self.repositorio.salvar(disciplina)

        ModeloDisciplina.objects.get(pk=disciplina.id.valor)

    def test_trazer_por_id_QUANDO_disciplina_existe_ENTAO_retorna_disciplina(self) -> None:
        modelo_disciplina: ModeloDisciplina = FabricaTesteModeloDisciplina.create()
        id_ = Id(modelo_disciplina.id)

        disciplina = self.repositorio.trazer_por_id(id_)

        self.assertEqual(disciplina.id, id_)

    def test_trazer_por_id_QUANDO_disciplina_nao_existe_ENTAO_lanca_erro_disciplina_nao_encontrada(self) -> None:
        id_ = FabricaTesteId.build()

        with self.assertRaises(ErroDisciplinaNaoEncontrada):
            self.repositorio.trazer_por_id(id_)
