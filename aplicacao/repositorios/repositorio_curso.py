from dominio.entidades import Curso
from dominio.objetos_de_valor import Id
from dominio.repositorios import RepositorioAbstratoCurso


class RepositorioCurso(RepositorioAbstratoCurso):
    def filtrar(self, **kwargs) -> [Curso]:
        pass

    def trazer_por_id(self, id_: Id) -> Curso:
        pass

    def salvar(self, curso: Curso) -> None:
        pass
