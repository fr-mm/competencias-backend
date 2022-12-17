from typing import List

from aplicacao.models import ModeloCompetencia, ModeloDocente
from dominio.entidades import Competencia
from dominio.objetos_de_valor import Id
from dominio.repositorios import RepositorioAbstratoCompetencia


class RepositorioCompetencia(RepositorioAbstratoCompetencia):
    def salvar(self, competencias: List[Competencia]) -> None:
        for competencia in competencias:
            ModeloCompetencia.de_entidade(competencia).save()

    def trazer_id_de_docente(self, id_docente: Id) -> List[Competencia]:
        modelo_docente = ModeloDocente.objects.get(pk=id_docente.valor)
        modelos = ModeloCompetencia.objects.filter(docente=modelo_docente)
        return [modelo.para_entidade() for modelo in modelos]

    def deletar_todos_de_docente(self, id_docente: Id) -> None:
        ModeloCompetencia.objects.filter(docente_id=id_docente.valor).delete()
