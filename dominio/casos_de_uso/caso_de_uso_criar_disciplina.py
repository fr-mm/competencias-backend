from dominio.otds import OTDDisciplinaEmCriacao, OTDDisciplina
from dominio.repositorios import RepositorioAbstratoDisciplina


class CasoDeUsoCriarDisciplina:
    __repositorio_disciplina: RepositorioAbstratoDisciplina

    def __init__(self, repositorio_disciplina: RepositorioAbstratoDisciplina) -> None:
        self.__repositorio_disciplina = repositorio_disciplina

    def executar(self, otd_disciplina_em_criacao: OTDDisciplinaEmCriacao) -> OTDDisciplina:
        disciplina = otd_disciplina_em_criacao.para_entidade()
        self.__repositorio_disciplina.salvar(disciplina)
        return OTDDisciplina.de_entidade(disciplina)
