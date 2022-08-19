from django.urls import path

from aplicacao.views import hello_world

urlpatterns = [
    path('', hello_world, name='index'),
]
