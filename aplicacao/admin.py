from django.contrib import admin

from aplicacao.models import ModeloDocente, ModeloTelefone, ModeloUnidadeSenai, ModeloDisciplina

admin.site.register(ModeloDocente)
admin.site.register(ModeloTelefone)
admin.site.register(ModeloUnidadeSenai)
admin.site.register(ModeloDisciplina)
