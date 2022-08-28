from unittest import TestCase
from urllib.request import Request
from uuid import uuid4
from mockito import mock, when, unstub

from aplicacao.views import DocenteView
from dominio.erros import ErroDocenteNaoEncontrado


class TestDocenteView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.container = mock({
            'casos_de_uso': mock({
                'trazer_docente': mock(),
                'desativar_docente': mock()
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
        when(self.container.casos_de_uso.trazer_docente).executar(id_).thenRaise(erro_docente_nao_encontrado)

        response = self.docente_view.get(request, id_)

        self.assertEqual(response.status_code, 404)

    def test_delete_QUANDO_docente_encontrado_ENTAO_retorna_status_200(self) -> None:
        request = Request(self.url)
        id_ = uuid4()

        response = self.docente_view.delete(request, id_)

        self.assertEqual(response.status_code, 200)

    def test_delete_QUANDO_docente_nao_encontrado_ENTAO_retorna_status_404(self) -> None:
        request = Request(self.url)
        id_ = uuid4()
        erro_docente_nao_encontrado = ErroDocenteNaoEncontrado(id_)
        when(self.container.casos_de_uso.desativar_docente).executar(id_).thenRaise(erro_docente_nao_encontrado)

        response = self.docente_view.delete(request, id_)

        self.assertEqual(response.status_code, 404)
