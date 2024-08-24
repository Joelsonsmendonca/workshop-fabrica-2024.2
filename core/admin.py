from django.contrib import admin
"""

Este arquivo contém a configuração do painel de administração do Django para os modelos Produto e Cliente.
Classe que define a configuração do painel de administração para o modelo Produto.

"""
from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'telefone', 'endereco')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

