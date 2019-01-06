from django.db import models

class Despesa(models.Model):
    TIPO_DESPESA_CHOICES = (
        ('Remédio', 'Remédio'),
        ('Roupas', 'Roupas'),
        ('Alimentação', 'Alimentação'),
        ('Educação', 'Educação'),
        ('Transporte', 'Transporte'),
        ('Outros', 'Outros'),
    )
    FORMA_PAGAMENTO_CHOICES = (
        ('Dinheiro', 'Dinheiro'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Cartão de Débito', 'Cartão de Débito'),
        ('Cartão Crediário', 'Cartão Crediário'),
        ('Cheque', 'Cheque'),
    )

    data_criacao = models.CharField('data de criacao',max_length=20)
    tipo_despesa = models.CharField('tipo de despesa',max_length=30, choices=TIPO_DESPESA_CHOICES)
    descricao = models.TextField('descricao', max_length=100)
    forma_pagamento = models.CharField('forma de pagamento',max_length=50, choices=FORMA_PAGAMENTO_CHOICES)
    vencimento = models.DateField()
    quitado = models.BooleanField()


    class Meta:
        verbose_name_plural = 'Despesas'
        verbose_name = 'Despesa'
        ordering = ('-vencimento', 'forma_pagamento',)

    def __str__(self):
        return '{} - {} - {}'.format(
            self.data_criacao,
            self.tipo_despesa, )
        self.descricao,

