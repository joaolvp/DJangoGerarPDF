from django.db import models

class Depto(models.Model):
    nome = models.CharField('Nome', max_length=50)
    andar = models.IntegerField('Andar')
    ramal = models.IntegerField('Ramal')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    TIPOS_FUNC = (
        ('Contador', 'CONTADOR'),
        ('Administrador', 'ADMINISTRADOR'),
        ('Economista', 'ECONOMISTA'),
        ('Outros', 'OUTROS'),
    )
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=70)
    funcao = models.CharField('Função', max_length=13, choices=TIPOS_FUNC)
    depto = models.ForeignKey(Depto, on_delete=models.CASCADE, verbose_name='funcionarios')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['depto', 'nome']

    def __str__(self):
        return self.nome + '' + self.sobrenome