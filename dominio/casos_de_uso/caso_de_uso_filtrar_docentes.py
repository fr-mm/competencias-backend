from dominio.otds import OTDDocente
from dominio.repositorios import RepositorioAbstratoDocente


class CasoDeUsoFiltrarDocentes:
    __repositorio_docente: RepositorioAbstratoDocente

    def __init__(self, repositorio_docente: RepositorioAbstratoDocente) -> None:
        self.__repositorio_docente = repositorio_docente

    def executar(self, ativo: bool = True, **kwargs) -> [OTDDocente]:
        docentes = self.__repositorio_docente.filtrar(ativo=ativo, **kwargs)
        return [OTDDocente.de_entidade(docente) for docente in docentes]
