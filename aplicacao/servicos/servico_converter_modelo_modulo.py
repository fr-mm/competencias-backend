from aplicacao.models import ModeloModulo, ModeloDisciplinaEmModulo
from dominio.entidades import Modulo


class ServicoConverterModeloModulo:
    @staticmethod
    def de_entidade(modulo: Modulo) -> ModeloModulo:
        return ModeloModulo(
            id=modulo.id.valor,
            numero=modulo.numero.valor,
        )

    @staticmethod
    def para_entidade(modelo: ModeloModulo) -> Modulo:
        disciplinas_em_modulo = ModeloDisciplinaEmModulo.objects.filter(modulo=modelo)
        return Modulo.construir(
            id_=modelo.id,
            numero=modelo.numero,
            disciplinas_ids=[disciplina_em_modulo.disciplina.id for disciplina_em_modulo in disciplinas_em_modulo],
        )
