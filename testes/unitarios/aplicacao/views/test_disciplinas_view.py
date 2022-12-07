from unittest import TestCase
from urllib.request import Request
from uuid import uuid4

from mockito import mock, unstub, when

from aplicacao.views import DisciplinasView
from dominio.erros import ErroDisciplinaNaoEncontrada
from dominio.otds import OTDDisciplina
from testes.fabricas import FabricaTesteOTDDisciplina, FabricaTesteOTDDisciplinaEmCriacao, FabricaTesteOTDIds


class TestDisciplinasView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.otd_disciplina: OTDDisciplina = FabricaTesteOTDDisciplina.build()
        self.container = mock({
            'casos_de_uso': mock({
                'disciplina': mock({
                    'criar': mock(),
                    'desativar': mock()
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

        esperado = otd_disciplina_criada.__dict__
        esperado['id'] = str(esperado['id'])
        self.assertEqual(response.data, otd_disciplina_criada.__dict__)

    def test_delete_QUANDO_disciplinas_existem_ENTAO_retorna_status_204(self) -> None:
        otd = FabricaTesteOTDIds.build()
        request = Request(self.url, data=otd.__dict__)

        response = self.view.delete(request)

        self.assertEqual(response.status_code, 204)

    def test_delete_QUANDO_payload_invalido_ENTAO_retorna_status_400(self) -> None:
        request = Request(self.url, data={})

        response = self.view.delete(request)

        self.assertEqual(response.status_code, 400)

    def test_delete_QUANDO_disciplinas_nao_existem_ENTAO_retorna_status_404(self) -> None:
        otd = FabricaTesteOTDIds.build()
        request = Request(self.url, data=otd.__dict__)
        erro_disciplina_nao_encontrada = ErroDisciplinaNaoEncontrada(uuid4())
        when(self.container.casos_de_uso.disciplina.desativar).executar(...).thenRaise(erro_disciplina_nao_encontrada)

        response = self.view.delete(request)

        self.assertEqual(response.status_code, 404)
