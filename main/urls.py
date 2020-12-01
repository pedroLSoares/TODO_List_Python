from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formAgenda',  views.formAgenda, name='formAgenda'),
    path('cria_tarefa', views.cria_tarefa, name='cria_tarefa'),
    path('atualizaTarefa', views.atualizaTarefa, name='atualizaTarefa'),
    path('atualizaTarefaCompleta/<str:diaSemana>/<int:id>', views.atualizaTarefaCompleta, name='atualizaTarefaCompleta'),
    path('editaTarefas/<str:diaSemana>', views.editaTarefas, name='editaTarefas'),
    path('excluiTarefa/<str:diaSemana>/<int:id>', views.excluiTarefa, name='excluiTarefa')
]
