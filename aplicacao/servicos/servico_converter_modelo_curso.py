from aplicacao.models import ModeloCurso, ModeloModuloEmCurso
from aplicacao.servicos.servico_converter_modelo_modulo import ServicoConverterModeloModulo
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
        modulos = [ServicoConverterModeloModulo.para_entidade(modulo_em_curso.modulo) for modulo_em_curso in modelos_modulo_em_curso]
        return Curso.construir(
            id_=modelo.id,
            nome=str(modelo.nome),
            modulos=modulos,
            ativo=bool(modelo.ativo)
        )
