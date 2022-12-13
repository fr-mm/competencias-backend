from unittest import TestCase
from urllib.request import Request

from mockito import mock, unstub, when

from aplicacao.serializers import SerializerOTDModulo
from aplicacao.views import CursoView
from dominio.entidades import Curso
from dominio.erros import ErroCursoNaoEncontrado
from dominio.otds import OTDCursoSaida, OTDCursoEntrada
from testes.fabricas import FabricaTesteCurso, FabricaTesteOTDCursoEntrada, FabricaTesteOTDCursoSaida


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

    @staticmethod
    def otd_curso_para_request_data(otd: OTDCursoEntrada) -> {any, any}:
        data = otd.__dict__
        modulos = []
        for otd_modulo in otd.modulos:
            modulo = otd_modulo.__dict__
            modulo['disciplinas_ids'] = [str(id_) for id_ in modulo['disciplinas_ids']]
            modulos.append(modulo)
        data['modulos'] = modulos
        return data

    def test_post_QUANDO_curso_encontrado_ENTAO_retorna_status_200(self) -> None:
        curso: Curso = FabricaTesteCurso.build()
        otd_entrada = FabricaTesteOTDCursoEntrada.build()
        data = self.otd_curso_para_request_data(otd_entrada)
        request = Request(self.url, data=data)
        otd_saida: OTDCursoSaida = FabricaTesteOTDCursoSaida.build(modulos=[])
        when(self.container.casos_de_uso.curso.editar).executar(...).thenReturn(otd_saida)

        response = self.view.post(request, curso.id.valor)

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_curso_nao_encontrado_ENTAO_retorna_status_404(self) -> None:
        otd: OTDCursoEntrada = FabricaTesteOTDCursoEntrada.build()
        erro_curso_nao_encontrado = ErroCursoNaoEncontrado(otd.id)
        when(self.container.casos_de_uso.curso.editar).executar(otd).thenRaise(erro_curso_nao_encontrado)
        data = self.otd_curso_para_request_data(otd)
        request = Request(self.url, data=data)

        response = self.view.post(request, otd.id)

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_sucesso_ENTAO_retorna_payload_esperado(self) -> None:
        otd: OTDCursoEntrada = FabricaTesteOTDCursoEntrada.build(modulos=[])
        data = self.otd_curso_para_request_data(otd)
        request = Request(self.url, data=data)
        when(self.container.casos_de_uso.curso.editar).executar(otd).thenReturn(otd)

        response = self.view.post(request, otd.id)

        response_data_esperado = data
        response_data_esperado['id'] = str(response_data_esperado['id'])
        self.assertEqual(response.data, data)

