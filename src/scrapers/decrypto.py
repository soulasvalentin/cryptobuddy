import requests
from shared import table_service

EXCHANGE = 'decrypto'

def scrap():    
    url = 'https://api.decrypto.com.ar:8081/1.0/frontend/precios/'
    res = requests.get(url)
    obj = res.json()

    for ticker in obj['data']:
        if ticker['origen'] == 2 and ticker['destino'] == 3:

            # ARS - BTC
            table_service.save_rates(EXCHANGE, 
                ticker['dcb'], 
                ticker['dca'], 
                'ARS', 'BTC')