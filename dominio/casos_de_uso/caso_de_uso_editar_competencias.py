from dominio.objetos_de_valor import Id
from dominio.otds import OTDCasoDeUsoEditarCompetencias
from dominio.repositorios import RepositorioAbstratoCompetencia


class CasoDeUsoEditarCompetencias:
    __repositorio_competencia: RepositorioAbstratoCompetencia

    def __init__(self, repositorio_competencia: RepositorioAbstratoCompetencia) -> None:
        self.__repositorio_competencia = repositorio_competencia

    def executar(self, otd: OTDCasoDeUsoEditarCompetencias) -> None:
        id_docente = Id(otd.docente_id)
        competencias = [otd_competencia.para_entidade() for otd_competencia in otd.competencias]
        self.__repositorio_competencia.deletar_todos_de_docente(id_docente)
        self.__repositorio_competencia.salvar(competencias)
