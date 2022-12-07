from django.urls import path

from aplicacao.views import DocentesView, DocenteView, DisciplinasView, DisciplinaView

urlpatterns = [
    path('docentes/', DocentesView.as_view(), name='docentes'),
    path('docentes/<uuid:id_>/', DocenteView.as_view(), name='docente'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('disciplina/<uuid:id_>', DisciplinaView.as_view(), name='disciplina'),
]
