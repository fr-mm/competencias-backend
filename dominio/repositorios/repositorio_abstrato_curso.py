from abc import abstractmethod, ABC

from dominio.entidades import Curso
from dominio.objetos_de_valor import Id


class RepositorioAbstratoCurso(ABC):
    @abstractmethod
    def filtrar(self, **kwargs) -> [Curso]:
        pass

    @abstractmethod
    def trazer_por_id(self, id_: Id) -> Curso:
        pass

    @abstractmethod
    def salvar(self, curso: Curso) -> None:
        pass
