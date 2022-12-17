from random import randint

import factory

from dominio.otds import OTDCasoDeUsoEditarCompetencias
from testes.fabricas.dominio.otds.fabrica_test_otd_competencia import FabricaTesteOTDCompetencia


class FabricaTesteOTDCasoDeUsoEditarCompetencias(factory.Factory):
    class Meta:
        model = OTDCasoDeUsoEditarCompetencias

    docente_id = factory.Faker('uuid4', cast_to=None)
    competencias = factory.List([factory.SubFactory(FabricaTesteOTDCompetencia) for _ in range(randint(1, 4))])
