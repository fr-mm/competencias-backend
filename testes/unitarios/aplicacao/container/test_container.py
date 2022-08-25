from django.test import TestCase

from aplicacao.container import container_de_dependencias
from dominio.repositorios import RepositorioAbstratoDocente


class TestContainer(TestCase):
    def test_container_nao_lanca_erro(self) -> None:
        repositorio_docentes = container_de_dependencias.repositorios.docentes

        self.assertIsInstance(repositorio_docentes, RepositorioAbstratoDocente)
