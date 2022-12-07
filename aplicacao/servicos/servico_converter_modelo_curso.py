from aplicacao.models import ModeloCurso, ModeloModuloEmCurso
from dominio.entidades import Curso


class ServicoConverterModeloCurso:
    @staticmethod
    def de_entidade(curso: Curso) -> ModeloCurso:
        return ModeloCurso(
            id=curso.id.valor,
            nome=curso.nome.valor,
            ativo=curso.ativo
        )

    @staticmethod
    def para_entidade(modelo: ModeloCurso) -> Curso:
        modelos_modulo_em_curso = ModeloModuloEmCurso.objects.filter(curso_id=modelo.id)
        return Curso.construir(
            id_=modelo.id,
            nome=str(modelo.nome),
            modulos_ids=[modulo_em_curso.modulo.id for modulo_em_curso in modelos_modulo_em_curso],
            ativo=bool(modelo.ativo)
        )
