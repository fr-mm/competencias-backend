from aplicacao.models import ModeloDocente
from dominio.entidades import Docente
from dominio.objetos_de_valor import IdDeDocente
from dominio.repositorios import RepositorioAbstratoDocente


class RepositorioDocente(RepositorioAbstratoDocente):
    def trazer_por_id(self, id_: IdDeDocente) -> Docente:
        pass

    def salvar(self, docente: Docente) -> None:
        modelo_docente = ModeloDocente.de_entidade(docente)
        modelo_docente.save()

    def deletar_por_id(self, id_: IdDeDocente) -> None:
        pass
