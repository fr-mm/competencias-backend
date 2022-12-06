from dominio.otds import OTDDisciplina
from dominio.repositorios import RepositorioAbstratoDisciplina


class CasoDeUsoEditarDisciplina:
    __repositorio_disciplina: RepositorioAbstratoDisciplina

    def __init__(self, repositorio_disciplina: RepositorioAbstratoDisciplina) -> None:
        self.__repositorio_disciplina = repositorio_disciplina

    def executar(self, otd_disciplina: OTDDisciplina) -> OTDDisciplina:
        disciplina = otd_disciplina.para_entidade()
        self.__repositorio_disciplina.trazer_por_id(disciplina.id)
        self.__repositorio_disciplina.salvar(disciplina)
        return otd_disciplina
