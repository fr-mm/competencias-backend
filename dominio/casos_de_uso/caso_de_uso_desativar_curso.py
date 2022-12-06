from uuid import UUID

from dominio.objetos_de_valor import Id
from dominio.repositorios import RepositorioAbstratoCurso


class CasoDeUsoDesativarCurso:
    __repositorio_curso: RepositorioAbstratoCurso

    def __init__(self, repositorio_curso: RepositorioAbstratoCurso) -> None:
        self.__repositorio_curso = repositorio_curso

    def executar(self, id_: UUID) -> None:
        id_curso = Id(id_)
        curso = self.__repositorio_curso.trazer_por_id(id_curso)
        curso.desativar()
        self.__repositorio_curso.salvar(curso)
