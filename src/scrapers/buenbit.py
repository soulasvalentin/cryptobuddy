import requests
from shared import table_service

EXCHANGE = 'buenbit'

def scrap():    
    url = 'https://be.buenbit.com/api/market/tickers/'
    res = requests.get(url)
    obj = res.json()

    # ARS - BTC
    table_service.save_rates(EXCHANGE, 
        float(obj['object']['btcars']['purchase_price']), 
        float(obj['object']['btcars']['selling_price']), 
        'ARS', 'BTC')