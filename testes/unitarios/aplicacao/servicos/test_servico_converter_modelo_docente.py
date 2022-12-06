from typing import List
from unittest import TestCase

import pytest

from aplicacao.models import ModeloUnidadeSenai, ModeloDocente, ModeloTelefone
from aplicacao.servicos import ServicoConverterModeloDocente
from dominio.entidades import Docente
from dominio.objetos_de_valor import Id
from testes.fabricas import FabricaTesteModeloUnidadeSenai, FabricaTesteDocente, FabricaTesteModeloDocente, \
    FabricaTesteModeloTelefone


@pytest.mark.django_db
class TestServicoConverterModeloDocente(TestCase):
    def test_de_entidade_QUANDO_entidade_fornecida_ENTAO_retorna_modelo_com_atributos_esperados(self) -> None:
        modelo_unidade_senai: ModeloUnidadeSenai = FabricaTesteModeloUnidadeSenai.create()
        docente: Docente = FabricaTesteDocente.build(unidade_senai_id=Id(modelo_unidade_senai.id))

        modelo_docente = ServicoConverterModeloDocente.de_entidade(entidade=docente)

        atributos_resultantes = [
            modelo_docente.id,
            modelo_docente.nome,
            modelo_docente.email,
            modelo_docente.unidade_senai.id,
            modelo_docente.tipo_de_contratacao,
            modelo_docente.ativo
        ]
        atributos_esperados = [
            docente.id.valor,
            docente.nome.valor,
            docente.email.valor,
            modelo_unidade_senai.id,
            docente.tipo_de_contratacao.valor.value,
            docente.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_para_entidade_QUANDO_chamado_ENTAO_retorna_entidade_com_atributos_esperados(self) -> None:
        modelo_unidade_senai: ModeloUnidadeSenai = FabricaTesteModeloUnidadeSenai.create()
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create(unidade_senai=modelo_unidade_senai)
        modelos_telefones: List[ModeloTelefone] = [
            FabricaTesteModeloTelefone.create(numero='(00)0000-0000', docente=modelo_docente),
            FabricaTesteModeloTelefone.create(numero='(11)1111-1111', docente=modelo_docente),
        ]

        docente = ServicoConverterModeloDocente.para_entidade(modelo_docente)

        atributos_resultantes = [
            docente.id.valor,
            docente.nome.valor,
            docente.email.valor,
            [telefone.valor for telefone in docente.telefones],
            modelo_unidade_senai.id,
            docente.tipo_de_contratacao.valor.value,
            docente.ativo
        ]
        atributos_esperados = [
            modelo_docente.id,
            modelo_docente.nome,
            modelo_docente.email,
            [telefone.numero for telefone in modelos_telefones],
            modelo_docente.unidade_senai.id,
            modelo_docente.tipo_de_contratacao,
            modelo_docente.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)