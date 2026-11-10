##
# Views apps / Receitas
##
from django.shortcuts import render, get_list_or_404

from .models import Receita

def lista_receitas(request):
    receitas = Receita.objects.filter(publicada=True)
    context = {
        "receitas" : receitas,
    }
    return render(request, "receitas/lista.html",context)
