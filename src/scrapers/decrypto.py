import logging
import requests
from shared import table_service

EXCHANGE = 'decrypto'
URL = 'https://api.decrypto.com.ar:8081/1.0/frontend/precios/'

def scrap(): 
    try:   
        res = requests.get(URL)
        obj = res.json()

        for ticker in obj['data']:
            # ARS - BTC
            if ticker['origen'] == 2 and ticker['destino'] == 3:
                table_service.save_rates(EXCHANGE, 
                    ticker['dcb'], 
                    ticker['dca'], 
                    'ARS', 'BTC')

            # USD - BTC
            if ticker['origen'] == 1 and ticker['destino'] == 3:                
                table_service.save_rates(EXCHANGE, 
                    round(ticker['dcb'], 2), 
                    round(ticker['dca'], 2), 
                    'USD', 'BTC')
    except:
        logging.error(f'"{EXCHANGE}" scraping failed')