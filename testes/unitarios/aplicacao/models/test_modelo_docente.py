from uuid import UUID
from django.test import TestCase

from testes.fabricas import FabricaTesteDocente, FabricaTesteModeloDocente
from aplicacao.models import ModeloDocente
from dominio.entidades import Docente


class TestModeloDocente(TestCase):
    def test_de_entidade_QUANDO_entidade_fornecida_ENTAO_retorna_modelo_com_atributos_esperados(self) -> None:
        docente: Docente = FabricaTesteDocente.build()

        modelo_docente = ModeloDocente.de_entidade(docente)

        atributos_resultantes = [
            modelo_docente.id,
            modelo_docente.nome,
            modelo_docente.ativo
        ]
        atributos_esperados = [
            docente.id.valor,
            docente.nome.valor,
            docente.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_para_entidade_QUANDO_chamado_ENTAO_retorna_entidade_com_atributos_esperados(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.build()

        docente = modelo_docente.para_entidade()

        atributos_resultantes = [
            docente.id.valor,
            docente.nome.valor,
            docente.ativo
        ]
        atributos_esperados = [
            UUID(modelo_docente.id),
            modelo_docente.nome,
            modelo_docente.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
