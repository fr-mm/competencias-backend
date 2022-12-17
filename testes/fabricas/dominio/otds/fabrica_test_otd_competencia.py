import factory

from dominio.otds import OTDCompetencia


class FabricaTesteOTDCompetencia(factory.Factory):
    class Meta:
        model = OTDCompetencia

    docente_id = factory.Faker('uuid4', cast_to=None)
    disciplina_id = factory.Faker('uuid4', cast_to=None)
    nivel = factory.Faker('pyint', min_value=2, max_value=4)
