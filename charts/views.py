import numpy as np
import pandas as pd
from django.shortcuts import render

import charts.le_cotacoes as lc
import charts.payoff_utils as pu


def home(request):
    # valores padrao caso não receba parametros GET
    # nome_moeda = 'Bitcoin'
    par_moedas = 'BTC-BRL'
    dias = '60'

    # par_moedas = 
    if 'par_moedas_form' in request.GET:
        par_moedas = request.GET['par_moedas_form']
    if 'dias_form' in request.GET:
        dias = request.GET['dias_form']

    dict_cotacoes = lc.cria_lista_de_cotacoes_por_qtd_dias(par_moedas, dias)
    dict_cotacoes['par_moedas'] = par_moedas
    dict_cotacoes['qtd_dias'] = dias

    # lista_moedas e lista_nomes 
    
    dict_cotacoes.update(lc.cria_lista_todos_pares_nomes())
    # print(dict_cotacoes)

    return render(request, 'charts/index.html', context = dict_cotacoes)

    
