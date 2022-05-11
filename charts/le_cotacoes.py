import json
from datetime import datetime

import requests


def cria_lista_de_cotacoes_por_qtd_dias(par_moedas, qtd_dias):
    objeto_cotacoes = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{par_moedas}/{qtd_dias}')
    # retorna todas as modedas disponíveis para análise
    # print(objeto_cotacoes.status_code)
    objeto_cotacoes = objeto_cotacoes.json()

    # Exemplo de retorno
    # {'high': '5.1619', 'low': '5.0784', 'varBid': '0.0845', 'pctChange': '1.66', 'bid': '5.1611', 'ask': '5.1626', 'timestamp': '1652129998'}

    dict_cotacoes = {}
    lista_cotacoes = []
    lista_datas = []

    for i , cotacao in enumerate(objeto_cotacoes):
        time_data = datetime.fromtimestamp(int(objeto_cotacoes[i]['timestamp']))
        lista_datas.append(time_data.strftime("%d/%m/%y"))       

    for i , cotacao in enumerate(objeto_cotacoes):
        lista_cotacoes.append(objeto_cotacoes[i]['bid'])

    dict_cotacoes = dict({"lista_cotacoes": list(reversed(lista_cotacoes)), "lista_datas": list(reversed(lista_datas))})

    return dict_cotacoes


def cria_lista_todos_pares_nomes():
    objeto_cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
    # retorna todas as modedas disponíveis para análise
    # print(objeto_cotacoes.status_code)
    dict_cotacoes_moedas = objeto_cotacoes.json()

    lista_moedas = []
    lista_nomes = []
    # itera mostrando todas as moedas possíveis
    for moeda in dict_cotacoes_moedas:
        lista_moedas.append(moeda)
    for moeda in lista_moedas:
        lista_nomes.append(dict_cotacoes_moedas[moeda]['name'].split('/')[0])

    dict_cotacoes = {}

    dict_cotacoes = dict({"lista_moedas": lista_moedas, "lista_nomes": lista_nomes})

    return dict_cotacoes
