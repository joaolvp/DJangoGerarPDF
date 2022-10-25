from django.contrib import admin
from .models import Depto, Funcionario

@admin.register(Depto)
class DeptoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'andar', 'ramal')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'funcao', 'depto')

    def nome_completo(self, func):
        return str(func)
