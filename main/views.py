from django.shortcuts import render, redirect
from .models import Tarefas
from datetime import date

# Create your views here.

def index(request):
    tarefas = Tarefas.objects.all()

    diasSemana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
    date.today()
    tarefasHoje = Tarefas.objects.filter(dia_da_semana=diasSemana[date.weekday(date.today())])
    data = date.weekday(date.today())
    tarefasAmanha = Tarefas.objects.filter(dia_da_semana=diasSemana[data + 1])


    dados = {
        'tarefasAmanha': tarefasAmanha,
        'tarefasHoje': tarefasHoje,
        'diasSemana': diasSemana,
        'tarefas': tarefas
    }
    return render(request, 'index.html', dados)

def formAgenda(request):
    return render(request, 'FormAgenda.html')

def cria_tarefa(request):
    if request.method == 'POST':
        tarefa = request.POST['tarefa']
        dia_da_semana = request.POST['dia_da_semana']
        tarefa = Tarefas.objects.create(tarefa=tarefa, dia_da_semana=dia_da_semana)
        tarefa.save()
        return redirect('index')


def atualizaTarefa(request):

    if request.method == 'POST':
        tarefas = Tarefas.objects.all()
        for tarefa in tarefas:
            if str(tarefa.id) in request.POST:
                tar = Tarefas.objects.get(pk=tarefa.id)
                tar.finalizado = True
                tar.save()
                print('Ta aqui')
            else:
                tar = Tarefas.objects.get(pk=tarefa.id)
                tar.finalizado = False
                tar.save()

    return redirect('index')

def editaTarefas(request, diaSemana):
    tarefas = Tarefas.objects.filter(dia_da_semana=diaSemana)
    diaSemana = diaSemana
    dados = {
        'tarefas': tarefas,
        'diaSemana': diaSemana
    }

    return render(request, 'FormEditaTarefa.html', dados)


def excluiTarefa(request, diaSemana ,id):
    tarefa = Tarefas.objects.get(pk=id)
    tarefa.delete()
    return redirect('editaTarefas', diaSemana)


def atualizaTarefaCompleta(request, diaSemana, id):
    tar = Tarefas.objects.get(pk=id)
    tar.tarefa = request.POST['tarefa']
    tar.dia_da_semana = request.POST['dia_da_semana']
    tar.save()

    return redirect('editaTarefas', diaSemana)