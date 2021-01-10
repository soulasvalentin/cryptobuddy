import requests
from shared import table_service

EXCHANGE = 'letsbit'

def scrap():    
    url = 'https://letsbit.io/api/v1/exchange/public/markets/tickers'
    res = requests.get(url)
    obj = res.json()
    buy = float(obj['btcars']['ticker']['buy'])
    sell = float(obj['btcars']['ticker']['sell'])

    table_service.save_current(EXCHANGE, buy, sell, 'ARS', 'BTC')
    table_service.save_history(EXCHANGE, buy, sell, 'ARS', 'BTC')