from django.contrib import admin

from aplicacao.models import ModeloDocente, ModeloUsuario, UsuarioBase


@admin.register(UsuarioBase)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(ModeloDocente)
admin.site.register(ModeloUsuario)
