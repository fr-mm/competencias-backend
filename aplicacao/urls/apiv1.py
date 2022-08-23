from django.urls import path

from aplicacao.views import DocentesView

urlpatterns = [
    path('docentes', DocentesView.as_view(), name='docentes'),
]
