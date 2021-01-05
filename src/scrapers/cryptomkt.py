import requests
from shared import table_service

EXCHANGE = 'cryptomkt'

def scrap():    
    url = 'https://api.cryptomkt.com/v1/ticker?market=BTCARS'
    res = requests.get(url)
    obj = res.json()
    buy = obj['data'][0]['bid']
    sell = obj['data'][0]['ask']

    table_service.save_current(EXCHANGE, buy, sell)
    table_service.save_history(EXCHANGE, buy, sell)