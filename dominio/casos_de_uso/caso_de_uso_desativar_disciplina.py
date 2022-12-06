from uuid import UUID

from dominio.objetos_de_valor import Id
from dominio.repositorios import RepositorioAbstratoDisciplina


class CasoDeUsoDesativarDisciplina:
    __repositorio_disciplina: RepositorioAbstratoDisciplina

    def __init__(self, repositorio_disciplina: RepositorioAbstratoDisciplina) -> None:
        self.__repositorio_disciplina = repositorio_disciplina

    def executar(self, id_: UUID) -> None:
        id_disciplina = Id(id_)
        disciplina = self.__repositorio_disciplina.trazer_por_id(id_disciplina)
        disciplina.desativar()
        self.__repositorio_disciplina.salvar(disciplina)
