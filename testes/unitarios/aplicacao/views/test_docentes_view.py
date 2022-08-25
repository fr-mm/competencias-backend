from urllib.request import Request
from mockito import mock
from rest_framework.test import APITestCase

from testes.fabricas import FabricaTesteOTDDocente
from aplicacao.views import DocentesView
from dominio.otds import OTDDocente


class TestDocentesView(APITestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.otd_docente: OTDDocente = FabricaTesteOTDDocente.build()
        self.container = mock({
            'casos_de_uso': mock({
                'criar_docente': mock({
                    'executar': lambda otd_entrada: self.otd_docente
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
