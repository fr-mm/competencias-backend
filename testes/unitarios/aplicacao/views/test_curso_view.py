from unittest import TestCase
from urllib.request import Request

from mockito import mock, unstub, when

from aplicacao.views import CursoView
from dominio.entidades import Curso
from dominio.erros import ErroCursoNaoEncontrado
from dominio.otds import OTDCurso
from testes.fabricas import FabricaTesteCurso, FabricaTesteOTDCurso


class TestCursoView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.container = mock({
            'casos_de_uso': mock({
                'curso': mock({
                    'editar': mock()
                })
            })
        })
        self.view = CursoView(self.container)

    def tearDown(self) -> None:
        unstub()

    def test_post_QUANDO_curso_encontrado_ENTAO_retorna_status_200(self) -> None:
        curso: Curso = FabricaTesteCurso.build()
        data = FabricaTesteOTDCurso.build().__dict__
        request = Request(self.url, data=data)

        response = self.view.post(request, curso.id.valor)

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_curso_nao_encontrado_ENTAO_retorna_status_404(self) -> None:
        otd: OTDCurso = FabricaTesteOTDCurso.build()
        erro_curso_nao_encontrado = ErroCursoNaoEncontrado(otd.id)
        when(self.container.casos_de_uso.curso.editar).executar(otd).thenRaise(erro_curso_nao_encontrado)
        request = Request(self.url, data=otd.__dict__)

        response = self.view.post(request, otd.id)

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_sucesso_ENTAO_retorna_payload_esperado(self) -> None:
        otd: OTDCurso = FabricaTesteOTDCurso.build()
        data = otd.__dict__
        request = Request(self.url, data=data)
        when(self.container.casos_de_uso.curso.editar).executar(otd).thenReturn(otd)

        response = self.view.post(request, otd.id)

        response_data_esperado = data
        response_data_esperado['id'] = str(response_data_esperado['id'])
        response_data_esperado['modulos_ids'] = [str(id_) for id_ in response_data_esperado['modulos_ids']]
        self.assertEqual(response.data, data)

