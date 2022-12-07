from django.urls import path

from aplicacao.views import DocentesView, DocenteView, DisciplinasView

urlpatterns = [
    path('docentes/', DocentesView.as_view(), name='docentes'),
    path('docentes/<uuid:id_>/', DocenteView.as_view(), name='docente'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas')
]
