from typing import List

from aplicacao.models import ModeloDisciplina
from dominio.entidades import Disciplina
from dominio.objetos_de_valor import Id
from dominio.repositorios import RepositorioAbstratoDisciplina


class RepositorioDisciplina(RepositorioAbstratoDisciplina):
    def filtrar(self, **kwargs) -> [Disciplina]:
        modelos_disciplinas: List[ModeloDisciplina] = ModeloDisciplina.objects.filter(**kwargs)
        return

    def salvar(self, disciplina: Disciplina) -> None:
        pass

    def trazer_por_id(self, id_: Id) -> Disciplina:
        pass
