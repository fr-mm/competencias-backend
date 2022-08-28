from uuid import UUID

from dominio.repositorios import RepositorioAbstratoDocente
from dominio.objetos_de_valor import IdDeDocente


class CasoDeUsoDesativarDocente:
    __repositorio_docente: RepositorioAbstratoDocente

    def __init__(self, repositorio_docente: RepositorioAbstratoDocente) -> None:
        self.__repositorio_docente = repositorio_docente

    def executar(self, id_: UUID) -> None:
        id_do_docente = IdDeDocente(id_)
        docente = self.__repositorio_docente.trazer_por_id(id_do_docente)
        docente.ativar()
        self.__repositorio_docente.salvar(docente)
