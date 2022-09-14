from django.urls import path

from aplicacao.views import DocentesView, DocenteView, UsuariosView

urlpatterns = [
    path('docentes/', DocentesView.as_view(), name='docentes'),
    path('docentes/<uuid:id_>/', DocenteView.as_view(), name='docente'),
    path('usuarios/', UsuariosView.as_view(), name='usuarios')
]
