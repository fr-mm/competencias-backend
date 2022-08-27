from dominio.otds import OTDDocente
from dominio.erros import ErroDocenteNaoEncontrado
from dominio.repositorios import RepositorioAbstratoDocente


class CasoDeUsoEditarDocente:
    __repositorio_docente: RepositorioAbstratoDocente

    def __init__(self, repositorio_docente: RepositorioAbstratoDocente) -> None:
        self.__repositorio_docente = repositorio_docente

    def executar(self, otd_docente: OTDDocente) -> None:
        docente = otd_docente.para_entidade()
        if self.__repositorio_docente.id_existe(docente.id):
            self.__repositorio_docente.salvar(docente)
        else:
            raise ErroDocenteNaoEncontrado(docente.id.valor)
