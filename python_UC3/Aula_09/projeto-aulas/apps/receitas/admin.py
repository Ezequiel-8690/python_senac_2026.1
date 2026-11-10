from django.contrib import admin

#Importação do modelo pro banco de dados 
from .models import Categoria,Receita

#Registro do modelo categoria no django 
admin.site.register(Categoria)

#Registro do modelo receita mo django 
admin.site.register(Receita)
