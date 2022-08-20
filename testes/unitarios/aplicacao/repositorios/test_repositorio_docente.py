from django.test import TestCase

from aplicacao.models import ModeloDocente
from aplicacao.repositorios import RepositorioDocente
from testes.fabricas.dominio.entidades import FabricaTesteDocente


class TestRepositorioDocente(TestCase):
    def setUp(self) -> None:
        self.repositorio_docente = RepositorioDocente()

    def test_salvar_QUANDO_docente_informado_ENTAO_salva_docente(self) -> None:
        docente = FabricaTesteDocente.build()

        self.repositorio_docente.salvar(docente)

        ModeloDocente.objects.get(pk=docente.id.valor)
