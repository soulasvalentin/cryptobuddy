import requests
from shared import table_service

EXCHANGE = 'buenbit'

def scrap():    
    url = 'https://be.buenbit.com/api/market/tickers/'
    res = requests.get(url)
    obj = res.json()
    buy = float(obj['object']['btcars']['purchase_price'])
    sell = float(obj['object']['btcars']['selling_price'])

    table_service.save_current(EXCHANGE, buy, sell, 'ARS', 'BTC')
    table_service.save_history(EXCHANGE, buy, sell, 'ARS', 'BTC')