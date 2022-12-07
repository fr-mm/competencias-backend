from unittest import TestCase
from urllib.request import Request

from mockito import mock, unstub, when

from aplicacao.views import DisciplinaView
from dominio.entidades import Disciplina
from dominio.erros import ErroDisciplinaNaoEncontrada
from dominio.otds import OTDDisciplina
from testes.fabricas import FabricaTesteOTDDisciplina, FabricaTesteDisciplina


class TestDisciplinaView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.container = mock({
            'casos_de_uso': mock({
                'disciplina': mock({
                    'editar': mock()
                })
            })
        })
        self.view = DisciplinaView(self.container)

    def tearDown(self) -> None:
        unstub()

    def test_post_QUANDO_disciplina_encontrada_ENTAO_retorna_status_200(self) -> None:
        disciplina: Disciplina = FabricaTesteDisciplina.build()
        data = FabricaTesteOTDDisciplina.build().__dict__
        request = Request(self.url, data=data)

        response = self.view.post(request, disciplina.id.valor)

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_disciplina_nao_encontrada_ENTAO_retorna_status_404(self) -> None:
        otd: OTDDisciplina = FabricaTesteOTDDisciplina.build()
        erro_disciplina_nao_encontrada = ErroDisciplinaNaoEncontrada(otd.id)
        when(self.container.casos_de_uso.disciplina.editar).executar(otd).thenRaise(erro_disciplina_nao_encontrada)
        request = Request(self.url, data=otd.__dict__)

        response = self.view.post(request, otd.id)

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_sucesso_ENTAO_retorna_payload_esperado(self) -> None:
        otd: OTDDisciplina = FabricaTesteOTDDisciplina.build()
        data = otd.__dict__
        request = Request(self.url, data=data)
        when(self.container.casos_de_uso.disciplina.editar).executar(otd).thenReturn(otd)

        response = self.view.post(request, otd.id)

        response_data_esperado = data
        response_data_esperado['id'] = str(response_data_esperado['id'])
        self.assertEqual(response.data, data)
