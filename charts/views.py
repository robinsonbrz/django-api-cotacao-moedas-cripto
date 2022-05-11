import numpy as np
import pandas as pd
from django.shortcuts import render

import charts.le_cotacoes as lc
import charts.payoff_utils as pu


def home(request):
    par_moedas = 'USD-BRL' 
    qtd_dias = '60'
    dict_cotacoes = lc.cria_lista_de_cotacoes_por_qtd_dias(par_moedas, qtd_dias)
    # print(dict_cotacoes)
    # context_dict = dict_cotacoes
    dict_cotacoes['par_moedas'] = 'USD-BRL' 
    dict_cotacoes['qtd_dias'] = '60'

    return render(request, 'charts/index.html', context = dict_cotacoes)
    
    
    # from charts.models import Ativo
    # p = Ativo.objects.all().order_by('-id')[:10]
