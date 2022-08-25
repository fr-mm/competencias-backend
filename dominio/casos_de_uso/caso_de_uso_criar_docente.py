from dominio.otds import OTDDocenteEmCriacao, OTDDocente
from dominio.repositorios import RepositorioAbstratoDocente


class CasoDeUsoCriarDocente:
    __repositorio_docente: RepositorioAbstratoDocente

    def __init__(self, repositorio_docente: RepositorioAbstratoDocente) -> None:
        self.__repositorio_docente = repositorio_docente

    def executar(self, otd_docente_em_criacao: OTDDocenteEmCriacao) -> OTDDocente:
        docente = otd_docente_em_criacao.para_entidade()
        self.__repositorio_docente.salvar(docente)
        return OTDDocente.de_entidade(docente)
