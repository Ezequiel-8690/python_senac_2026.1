from django.contrib import admin
from .models import (
    Categoria,
    Cliente,
    ComentarioAvaliacao,
    Pedido,
    EnderecoEntrega,
    Produto,
    ItemPedido,
)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    #Colunas exibidas na listagem
    list_display = ["id","nome","descricao"]
    #Campos de pesquisa na caixa de busca 
    search_fields = ["nome","descricao"]
    #Ordenação padrão da listagem
    ordering = ["nome"]

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = ["usuario",
                    "telefone",
                    "sexo",
                    "cpf",
                    "data_nascimento"]
    search_fields = ["usuario",
                     "sexo",
                     "nome_social"]
    ordering = ["usuario"]

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):

    list_display = ["status",
                    "endereco_entrega",
                    "atualizado_em"]
    search_fields = ["cirado_em",
                     "status",
                     "atualizado_em"]
    ordering = ["status"]

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):

    list_display = ["pedido",
                    "quantidade",
                    "preco_unitario",
                    "produto"]
    search_fields = ["pedido",
                     "produto"]
    ordering = ["quantidade"]

# @admin.register(ComentarioAvaliacao)
# class ComentarioAvaliacaoAdmin(admin.ModelAdmin):

#     list_display = ["nome"]
#     search_fields = ["nome"]
#     ordering = ["nome"]

# @admin.register(EnderecoEntrega)
# class EnderecoEntregaAdmin(admin.ModelAdmin):

#     list_display = ["nome"]
#     search_fields = ["nome"]
#     ordering = ["nome"]

# @admin.register(Produto)
# class ProdutoAdmin(admin.ModelAdmin):

#     list_display = ["nome"]
#     search_fields = ["nome"]
#     ordering = ["nome"]