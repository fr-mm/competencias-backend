from django.urls import path

from aplicacao.views import DocentesView

urlpatterns = [
    path('docentes/', DocentesView.as_view(), name='docentes'),
    path('docentes/<uuid:id_de_docente>')
]
