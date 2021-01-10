import requests
from shared import table_service

EXCHANGE = 'cryptomkt'

def scrap():    
    url = 'https://api.cryptomkt.com/v1/ticker'
    res = requests.get(url)
    obj = res.json()

    for ticker in obj['data']:
        # ARS - BTC
        if ticker['market'] == 'BTCARS':            
            table_service.save_rates(EXCHANGE, 
                float(ticker['bid']), 
                float(ticker['ask']), 
                'ARS', 'BTC')

        # ARS - ETH
        if ticker['market'] == 'ETHARS':            
            table_service.save_rates(EXCHANGE, 
                float(ticker['bid']), 
                float(ticker['ask']), 
                'ARS', 'ETH')