from typing import List

from aplicacao.models import ModeloDisciplina
from dominio.entidades import Disciplina
from dominio.erros import ErroDisciplinaNaoEncontrada
from dominio.objetos_de_valor import Id
from dominio.repositorios import RepositorioAbstratoDisciplina


class RepositorioDisciplina(RepositorioAbstratoDisciplina):
    def filtrar(self, **kwargs) -> [Disciplina]:
        modelos_disciplinas: List[ModeloDisciplina] = ModeloDisciplina.objects.filter(**kwargs)
        return [modelo.para_entidade() for modelo in modelos_disciplinas]

    def trazer_por_id(self, id_: Id) -> Disciplina:
        try:
            modelo: ModeloDisciplina = ModeloDisciplina.objects.get(pk=id_.valor)
            return modelo.para_entidade()
        except ModeloDisciplina.DoesNotExist:
            raise ErroDisciplinaNaoEncontrada(id_.valor)

    def salvar(self, disciplina: Disciplina) -> None:
        modelo_disciplina = ModeloDisciplina.de_entidade(disciplina)
        modelo_disciplina.save()
