from collections import OrderedDict
from unittest import TestCase
from urllib.request import Request

from mockito import mock, when

from aplicacao.views import DocentesView
from dominio.otds import OTDDocente, OTDDocenteEmCriacao
from testes.fabricas import FabricaTesteOTDDocente, FabricaTesteOTDDocenteEmCriacao


class TestDocentesView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.otd_docente: OTDDocente = FabricaTesteOTDDocente.build()
        self.container = mock({
            'casos_de_uso': mock({
                'criar_docente': mock(),
                'filtrar_docentes': mock()
            })
        })
        self.docentes_view = DocentesView(self.container)

    def test_post_QUANDO_request_valida_ENTAO_retorna_status_201(self) -> None:
        data = FabricaTesteOTDDocenteEmCriacao.build().__dict__
        request = Request(self.url, data=data)

        response = self.docentes_view.post(request)

        self.assertEqual(response.status_code, 201)

    def test_post_QUANDO_request_valida_ENTAO_retorna_response_contendo_docente_com_atributos_esperados(self) -> None:
        otd_docente_em_criacao: OTDDocenteEmCriacao = FabricaTesteOTDDocenteEmCriacao.build()
        data = otd_docente_em_criacao.__dict__
        request = Request(self.url, data=data)
        otd_docente_criado: OTDDocente = FabricaTesteOTDDocente.build(nome=otd_docente_em_criacao.nome)
        when(self.container.casos_de_uso.criar_docente).executar(otd_docente_em_criacao).thenReturn(otd_docente_criado)

        response = self.docentes_view.post(request)

        atributos_resultantes = [
            response.data['nome']
        ]
        atributos_esperados = [
            otd_docente_em_criacao.nome
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_post_QUANDO_request_invalida_ENTAO_retorna_status_400(self) -> None:
        data = {
            'nome': ''
        }
        request = Request(self.url, data=data)

        response = self.docentes_view.post(request)

        self.assertEqual(response.status_code, 400)

    def test_get_QUANDO_request_recebida_ENTAO_retorna_status_200(self) -> None:
        request = Request(self.url)

        response = self.docentes_view.get(request)

        self.assertEqual(response.status_code, 200)

    def test_get_QUANDO_request_recebida_ENTAO_retorna_response_com_docentes_ativos(self) -> None:
        otds_docente: [OTDDocente] = [FabricaTesteOTDDocente.build(ativo=True) for _ in range(2)]
        when(self.container.casos_de_uso.filtrar_docentes).executar(ativo=True).thenReturn(otds_docente)
        request = Request(self.url)

        response = self.docentes_view.get(request)

        response_data_esperado = [
            OrderedDict([
                ('id', str(otd.id)),
                ('nome', otd.nome),
                ('email', otd.email),
                ('telefones', otd.telefones),
                ('tipo_de_contratacao', otd.tipo_de_contratacao),
                ('unidade_senai_id', str(otd.unidade_senai_id)),
                ('ativo', otd.ativo)
            ]) for otd in otds_docente
        ]
        self.assertEqual(response.data, response_data_esperado)

