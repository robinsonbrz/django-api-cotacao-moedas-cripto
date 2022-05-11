import numpy as np
import pandas as pd
from django.shortcuts import render

import charts.le_cotacoes as lc
import charts.payoff_utils as pu


def home(request):
    dict_cotacoes = lc.cria_lista_de_cotacoes()
    # print(dict_cotacoes)
    
    return render(request, 'charts/index.html', context=dict_cotacoes)
    
    
    # from charts.models import Ativo
    # p = Ativo.objects.all().order_by('-id')[:10]
