import json
from datetime import datetime

import requests


def cria_lista_de_cotacoes():
    objeto_cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/60')
    # retorna todas as modedas disponíveis para análise
    # print(objeto_cotacoes.status_code)
    objeto_cotacoes = objeto_cotacoes.json()

    # Exemplo de retorno
    # {'high': '5.1619', 'low': '5.0784', 'varBid': '0.0845', 'pctChange': '1.66', 'bid': '5.1611', 'ask': '5.1626', 'timestamp': '1652129998'}

    print(len(objeto_cotacoes))
    dict_cotacoes = {}
    lista_cotacoes = []
    lista_datas = []
    for i , cotacao in enumerate(objeto_cotacoes):
        lista_cotacoes.append(objeto_cotacoes[i]['bid'])
    for i , cotacao in enumerate(objeto_cotacoes):
        lista_datas.append(objeto_cotacoes[i]['timestamp'])        

    dict_cotacoes = dict({"lista_cotacoes": lista_cotacoes, "lista_datas": lista_datas})

    return dict_cotacoes
