from dominio.otds import OTDDocente
from dominio.repositorios import RepositorioAbstratoDocente


class CasoDeUsoTrazerDocentes:
    __repositorio_docente: RepositorioAbstratoDocente

    def __init__(self, repositorio_docente: RepositorioAbstratoDocente) -> None:
        self.__repositorio_docente = repositorio_docente

    def executar(self) -> [OTDDocente]:
        docentes = self.__repositorio_docente.trazer()
        return [OTDDocente.de_entidade(docente) for docente in docentes]
