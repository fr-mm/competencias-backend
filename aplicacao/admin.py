from django.contrib import admin

from aplicacao.models import ModeloDocente, ModeloTelefone, ModeloUnidadeSenai

admin.site.register(ModeloDocente)
admin.site.register(ModeloTelefone)
admin.site.register(ModeloUnidadeSenai)
