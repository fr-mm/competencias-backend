from uuid import UUID

from dominio.otds import OTDDocente
from dominio.erros import ErroDocenteNaoEncontrado
from dominio.repositorios import RepositorioAbstratoDocente
from dominio.objetos_de_valor import IdDeDocente


class CasoDeUsoTrazerDocente:
    __repositorio_docente: RepositorioAbstratoDocente

    def __init__(self, repositorio_docente: RepositorioAbstratoDocente) -> None:
        self.__repositorio_docente = repositorio_docente

    def executar(self, id_: UUID) -> OTDDocente:
        id_de_docente = IdDeDocente(id_)
        if self.__repositorio_docente.id_existe(id_de_docente):
            docente = self.__repositorio_docente.trazer_por_id(id_de_docente)
            return OTDDocente.de_entidade(docente)
        else:
            raise ErroDocenteNaoEncontrado(id_)
