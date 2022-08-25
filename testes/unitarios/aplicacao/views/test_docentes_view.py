from unittest import TestCase
from urllib.request import Request
from mockito import mock, when

from testes.fabricas import FabricaTesteOTDDocente
from aplicacao.views import DocentesView
from dominio.otds import OTDDocente


class TestDocentesView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.otd_docente: OTDDocente = FabricaTesteOTDDocente.build()
        self.container = mock({
            'casos_de_uso': mock({
                'criar_docente': mock({
                    'executar': lambda otd_entrada: self.otd_docente
                }),
                'trazer_docentes': mock({
                    'executar': lambda: None
                })
            })
        })
        self.docentes_view = DocentesView(self.container)

    def test_post_QUANDO_request_valida_ENTAO_retorna_status_201(self) -> None:
        data = {
            'nome': 'Nome Falso'
        }
        request = Request(self.url, data=data)

        response = self.docentes_view.post(request)

        self.assertEqual(response.status_code, 201)

    def test_post_QUANDO_invalida_ENTAO_retorna_status_400(self) -> None:
        data = {
            'nome': ''
        }
        request = Request(self.url, data=data)

        response = self.docentes_view.post(request)

        self.assertEqual(response.status_code, 400)

    def test_get_QUANDO_chamado_ENTAO_retorna_status_201(self) -> None:
        request = Request(self.url)

        response = self.docentes_view.get(request)

        self.assertEqual(response.status_code, 201)

    def test_get_QUANDO_chamado_ENTAO_retorna_respopnse_com_conteudo_esperado(self) -> None:
        otds_docente: [OTDDocente] = [FabricaTesteOTDDocente.build() for _ in range(2)]
        when(self.container.casos_de_uso.trazer_docentes).executar().thenReturn(otds_docente)
        request = Request(self.url)

        response = self.docentes_view.get(request)

        response_data_esperado = [
            {
                'id': otd.id,
                'nome': otd.nome
            } for otd in otds_docente
        ]
        self.assertEqual(response.data, response_data_esperado)

