from django.db import models

# Create your models here.

class Tarefas(models.Model):
    tarefa =models.CharField(max_length=200)
    dia_da_semana = models.CharField(max_length=100)
    finalizado = models.BooleanField(default=False)
