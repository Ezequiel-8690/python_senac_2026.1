from django.urls import path
from . import views     # Importando as views da aplicação de páginas estáticas

app_name = 'apps.produtos'  # Cria um namespace para as urls da aplicação de páginas estáticas

urlpatterns = [
    path("", views.home, name="home"),]