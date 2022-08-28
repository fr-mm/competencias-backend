from uuid import UUID

from django.test import TestCase

from dominio.entidades import Docente
from dominio.erros import ErroDocenteNaoEncontrado
from dominio.objetos_de_valor import IdDeDocente, NomeDeDocente
from testes.fabricas import FabricaTesteModeloDocente, FabricaTesteDocente, FabricaTesteIdDeDocente
from aplicacao.models import ModeloDocente
from aplicacao.repositorios import RepositorioDocente


class TestRepositorioDocente(TestCase):
    def setUp(self) -> None:
        self.repositorio_docente = RepositorioDocente()

    def test_filtrar_QUANDO_nenhum_filtro_informado_ENTAO_retorna_todos_os_docentes(self) -> None:
        quantidade = 2
        [FabricaTesteModeloDocente.create() for _ in range(quantidade)]

        docentes = self.repositorio_docente.filtrar()

        self.assertEqual(len(docentes), quantidade)

    def test_filtrar_QUANDO_filtrar_por_ativo_true_ENTAO_retorna_docentes_ativos(self) -> None:
        modelos_docentes_ativos: [ModeloDocente] = [FabricaTesteModeloDocente.create(ativo=True) for _ in range(2)]
        [FabricaTesteModeloDocente.create(ativo=False) for _ in range(2)]

        docentes = self.repositorio_docente.filtrar(ativo=True)

        ids_resultantes = [docente.id.valor for docente in docentes]
        ids_esperados = [UUID(modelo.id) for modelo in modelos_docentes_ativos]
        self.assertEqual(ids_resultantes, ids_esperados)

    def test_salvar_QUANDO_docente_informado_ENTAO_salva_docente(self) -> None:
        docente = FabricaTesteDocente.build()

        self.repositorio_docente.salvar(docente)

        ModeloDocente.objects.get(pk=docente.id.valor)

    def test_trazer_por_id_QUANDO_docente_existe_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        modelo: ModeloDocente = FabricaTesteModeloDocente.create()
        id_do_docente = IdDeDocente(UUID(modelo.id))

        docente = self.repositorio_docente.trazer_por_id(id_do_docente)

        atributos_resultantes = [
            docente.id,
            docente.nome,
            docente.ativo
        ]
        atributos_esperados = [
            IdDeDocente(UUID(modelo.id)),
            NomeDeDocente(modelo.nome),
            modelo.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_trazer_por_id_QUANDO_docente_nao_existe_ENTAO_lanca_erro_docente_nao_encontrado(self) -> None:
        id_do_docente: IdDeDocente = FabricaTesteIdDeDocente.build()

        with self.assertRaises(ErroDocenteNaoEncontrado):
            self.repositorio_docente.trazer_por_id(id_do_docente)
