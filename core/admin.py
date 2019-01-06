from django.contrib import admin

from core.models import Despesa
from datetime import date

data_atual = date.today()


class DespesaAdmin(admin.ModelAdmin):
    list_display = (
        'data_criacao', 'tipo_despesa', 'descricao', 'vencimento', 'forma_pagamento', 'quitado', 'conta_prox_vencimento'
    )
    list_filter = ('vencimento','quitado',)

    def conta_prox_vencimento(self, obj):
        return obj.vencimento <= (data_atual)

    conta_prox_vencimento.short_description = 'Próximo a vencer?'
    conta_prox_vencimento.boolean = True


admin.site.register(Despesa, DespesaAdmin)

admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Despesas de Ana'
admin.site.site_title = 'Despesas de Ana'