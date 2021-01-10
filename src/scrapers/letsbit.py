import requests
from shared import table_service

EXCHANGE = 'letsbit'

def scrap():    
    url = 'https://letsbit.io/api/v1/exchange/public/markets/tickers'
    res = requests.get(url)
    obj = res.json()

    # ARS - BTC
    table_service.save_rates(EXCHANGE, 
        float(obj['btcars']['ticker']['buy']), 
        float(obj['btcars']['ticker']['sell']), 
        'ARS', 'BTC')

    # ARS - ETH
    table_service.save_rates(EXCHANGE, 
        float(obj['ethars']['ticker']['buy']), 
        float(obj['ethars']['ticker']['sell']), 
        'ARS', 'ETH')