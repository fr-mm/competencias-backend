from uuid import UUID

from django.test import TestCase

from aplicacao.models import ModeloDocente
from dominio.entidades import Docente
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_docente import FabricaTesteModeloDocente
from testes.fabricas.dominio.entidades import FabricaTesteDocente


class TestModeloDocente(TestCase):
    def test_de_entidade_QUANDO_entidade_fornecida_ENTAO_retorna_modelo_com_atributos_esperados(self) -> None:
        docente: Docente = FabricaTesteDocente.build()

        modelo_docente = ModeloDocente.de_entidade(docente)

        atributos_resultantes = [
            modelo_docente.nome,
            modelo_docente.id
        ]
        atributos_esperados = [
            docente.nome.valor,
            docente.id.valor
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_para_entidade_QUANDO_chamado_ENTAO_retorna_entidade_com_atributos_esperados(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.build()

        docente = modelo_docente.para_entidade()

        atributos_resultantes = [
            docente.nome.valor,
            docente.id.valor
        ]
        atributos_esperados = [
            modelo_docente.nome,
            UUID(modelo_docente.id)
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
