import pytest
from django.test import TestCase

from aplicacao.models import ModeloDocente, ModeloUnidadeSenai, ModeloTelefone
from aplicacao.repositorios import RepositorioDocente
from dominio.entidades import Docente
from dominio.erros import ErroDocenteNaoEncontrado
from dominio.objetos_de_valor import Id, NomeDeDocente, Telefone
from testes.fabricas import FabricaTesteModeloDocente, FabricaTesteDocente, FabricaTesteId, \
    FabricaTesteModeloUnidadeSenai, FabricaTesteModeloTelefone


@pytest.mark.django_db
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
        ids_esperados = [modelo.id for modelo in modelos_docentes_ativos]
        self.assertEqual(ids_resultantes, ids_esperados)

    def test_salvar_QUANDO_docente_informado_ENTAO_salva_docente(self) -> None:
        modelo_unidade_senai: ModeloUnidadeSenai = FabricaTesteModeloUnidadeSenai.create()
        docente = FabricaTesteDocente.build(unidade_senai_id=Id(modelo_unidade_senai.id))

        self.repositorio_docente.salvar(docente)

        ModeloDocente.objects.get(pk=docente.id.valor)

    def test_salvar_QUANDO_telefones_mudaram_ENTAO_atualiza_telefones(self) -> None:
        telefones_novos = ['(11)1111-1111', '(22)2222-2222']
        modelo_unidade_senai: ModeloUnidadeSenai = FabricaTesteModeloUnidadeSenai.create()
        docente: Docente = FabricaTesteDocente.build(
            telefones=[Telefone(telefone) for telefone in telefones_novos],
            unidade_senai_id=Id(modelo_unidade_senai.id)
        )
        modelo_docente = FabricaTesteModeloDocente.create(
            id=docente.id.valor,
            nome=docente.nome.valor,
            email=docente.email.valor,
            unidade_senai=modelo_unidade_senai,
            tipo_de_contratacao=docente.tipo_de_contratacao.valor.value,
            ativo=docente.ativo
        )
        FabricaTesteModeloTelefone.create(
            docente=modelo_docente,
            numero='(00)0000-0000'
        )

        self.repositorio_docente.salvar(docente)

        modelos_telefones = ModeloTelefone.objects.filter(docente_id=docente.id.valor)
        telefones = [modelo.numero for modelo in modelos_telefones]
        self.assertEqual(telefones, telefones_novos)

    def test_trazer_por_id_QUANDO_docente_existe_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        modelo: ModeloDocente = FabricaTesteModeloDocente.create()
        id_do_docente = Id(modelo.id)

        docente = self.repositorio_docente.trazer_por_id(id_do_docente)

        atributos_resultantes = [
            docente.id,
            docente.nome,
            docente.ativo
        ]
        atributos_esperados = [
            Id(modelo.id),
            NomeDeDocente(modelo.nome),
            modelo.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_trazer_por_id_QUANDO_docente_nao_existe_ENTAO_lanca_erro_docente_nao_encontrado(self) -> None:
        id_do_docente: Id = FabricaTesteId.build()

        with self.assertRaises(ErroDocenteNaoEncontrado):
            self.repositorio_docente.trazer_por_id(id_do_docente)
