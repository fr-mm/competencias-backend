from unittest import TestCase
from urllib.request import Request

from mockito import mock, unstub, when

from aplicacao.views import DisciplinasView
from dominio.otds import OTDDisciplina
from testes.fabricas import FabricaTesteOTDDisciplina, FabricaTesteOTDDisciplinaEmCriacao


class TestDisciplinasView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.otd_disciplina: OTDDisciplina = FabricaTesteOTDDisciplina.build()
        self.container = mock({
            'casos_de_uso': mock({
                'disciplina': mock({
                    'criar': mock()
                })
            })
        })
        self.view = DisciplinasView(self.container)

    def tearDown(self) -> None:
        unstub()

    def test_post_QUANDO_request_valida_ENTAO_retorna_status_201(self) -> None:
        data = FabricaTesteOTDDisciplinaEmCriacao.build().__dict__
        request = Request(self.url, data=data)

        response = self.view.post(request)

        self.assertEqual(response.status_code, 201)

    def test_post_QUANDO_request_valida_ENTAO_retorna_response_contendo_disciplina_com_atributos_esperados(self) -> None:
        otd_disciplina_em_criacao = FabricaTesteOTDDisciplinaEmCriacao.build()
        otd_disciplina_criada: OTDDisciplina = FabricaTesteOTDDisciplina.build()
        when(self.container.casos_de_uso.disciplina.criar).executar(otd_disciplina_em_criacao).thenReturn(otd_disciplina_criada)
        data = otd_disciplina_em_criacao.__dict__
        request = Request(self.url, data=data)

        response = self.view.post(request)

        self.assertEqual(response.data, otd_disciplina_criada.__dict__)
