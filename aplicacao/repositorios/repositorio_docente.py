from aplicacao.models import ModeloDocente
from dominio.erros import ErroDocenteNaoEncontrado
from dominio.repositorios import RepositorioAbstratoDocente
from dominio.entidades import Docente
from dominio.objetos_de_valor import IdDeDocente


class RepositorioDocente(RepositorioAbstratoDocente):
    def filtrar(self, **kwargs) -> [Docente]:
        modelos = ModeloDocente.objects.filter(**kwargs)
        return [modelo.para_entidade() for modelo in modelos]

    def trazer_por_id(self, id_: IdDeDocente) -> Docente:
        try:
            modelo = ModeloDocente.objects.get(pk=id_.valor)
            return modelo.para_entidade()
        except ModeloDocente.DoesNotExist:
            raise ErroDocenteNaoEncontrado(id_.valor)

    def salvar(self, docente: Docente) -> None:
        modelo = ModeloDocente.de_entidade(docente)
        modelo.save()
