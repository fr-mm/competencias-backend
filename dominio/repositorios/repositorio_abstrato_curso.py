from abc import abstractmethod, ABC

from dominio.entidades import Docente, Curso
from dominio.objetos_de_valor import Id


class RepositorioAbstratoCurso(ABC):
    @abstractmethod
    def filtrar(self, **kwargs) -> [Docente]:
        pass

    @abstractmethod
    def trazer_por_id(self, id_: Id) -> Docente:
        """Lança ErroDocenteNaoEncontrado"""
        pass

    @abstractmethod
    def salvar(self, curso: Curso) -> None:
        pass
