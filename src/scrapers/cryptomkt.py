import requests
from shared import table_service

EXCHANGE = 'cryptomkt'

def scrap():    
    url = 'https://api.cryptomkt.com/v1/ticker?market=BTCARS'
    res = requests.get(url)
    obj = res.json()
    buy = float(obj['data'][0]['bid'])
    sell = float(obj['data'][0]['ask'])

    table_service.save_current(EXCHANGE, buy, sell, 'ARS', 'BTC')
    table_service.save_history(EXCHANGE, buy, sell, 'ARS', 'BTC')