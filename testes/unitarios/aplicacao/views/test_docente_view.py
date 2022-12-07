from unittest import TestCase
from urllib.request import Request
from uuid import uuid4
from mockito import mock, when, unstub

from aplicacao.views import DocenteView
from dominio.entidades import Docente
from dominio.erros import ErroDocenteNaoEncontrado
from dominio.otds import OTDDocente
from testes.fabricas import FabricaTesteDocente, FabricaTesteOTDDocente


class TestDocenteView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.container = mock({
            'casos_de_uso': mock({
                'docente': mock({
                    'trazer': mock(),
                    'editar': mock(),
                    'desativar': mock()
                })
            })
        })
        self.docente_view = DocenteView(self.container)

    def tearDown(self) -> None:
        unstub()

    def test_get_QUANDO_docente_encontrado_ENTAO_retorna_status_200(self) -> None:
        request = Request(self.url)
        id_ = uuid4()

        response = self.docente_view.get(request, id_)

        self.assertEqual(response.status_code, 200)

    def test_get_QUANDO_docente_nao_encontrado_ENTAO_retorna_status_404(self) -> None:
        request = Request(self.url)
        id_ = uuid4()
        erro_docente_nao_encontrado = ErroDocenteNaoEncontrado(id_)
        when(self.container.casos_de_uso.docente.trazer).executar(id_).thenRaise(erro_docente_nao_encontrado)

        response = self.docente_view.get(request, id_)

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_docente_encontrado_ENTAO_retorna_status_200(self) -> None:
        docente: Docente = FabricaTesteDocente.build()
        data = FabricaTesteOTDDocente.build().__dict__
        request = Request(self.url, data=data)

        response = self.docente_view.post(request, docente.id.valor)

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_docente_nao_encontrado_ENTAO_retorna_status_404(self) -> None:
        otd_docente: OTDDocente = FabricaTesteOTDDocente.build()
        data = otd_docente.__dict__
        erro_docente_nao_encontrado = ErroDocenteNaoEncontrado(otd_docente.id)
        when(self.container.casos_de_uso.docente.editar).executar(otd_docente).thenRaise(erro_docente_nao_encontrado)
        request = Request(self.url, data=data)

        response = self.docente_view.post(request, otd_docente.id)

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_sucesso_ENTAO_retorna_payload_esperado(self) -> None:
        otd_docente: OTDDocente = FabricaTesteOTDDocente.build()
        data = otd_docente.__dict__
        request = Request(self.url, data=data)
        when(self.container.casos_de_uso.docente.editar).executar(otd_docente).thenReturn(otd_docente)

        response = self.docente_view.post(request, otd_docente.id)

        response_data_esperado = data
        response_data_esperado['id'] = str(response_data_esperado['id'])
        self.assertEqual(response.data, data)

    def test_delete_QUANDO_docente_encontrado_ENTAO_retorna_status_200(self) -> None:
        request = Request(self.url)
        id_ = uuid4()

        response = self.docente_view.delete(request, id_)

        self.assertEqual(response.status_code, 200)

    def test_delete_QUANDO_docente_nao_encontrado_ENTAO_retorna_status_404(self) -> None:
        request = Request(self.url)
        id_ = uuid4()
        erro_docente_nao_encontrado = ErroDocenteNaoEncontrado(id_)
        when(self.container.casos_de_uso.docente.desativar).executar(id_).thenRaise(erro_docente_nao_encontrado)

        response = self.docente_view.delete(request, id_)

        self.assertEqual(response.status_code, 404)
