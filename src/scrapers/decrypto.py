import requests
from shared import table_service

EXCHANGE = 'decrypto'

def scrap():    
    url = 'https://api.decrypto.com.ar:8081/1.0/frontend/precios/'
    res = requests.get(url)
    tickers = res.json()['data']
    for ticker in tickers:
        if ticker['origen'] == 2 and ticker['destino'] == 3:
            buy = ticker['dcb']
            sell = ticker['dca']

            table_service.save_current(EXCHANGE, buy, sell)
            table_service.save_history(EXCHANGE, buy, sell)