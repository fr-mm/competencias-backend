from uuid import uuid4

import factory

from aplicacao.otds import OTDIds


class FabricaTesteOTDIds(factory.Factory):
    class Meta:
        model = OTDIds

    ids = factory.List([uuid4() for _ in range(3)])
