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
            if ticker['origen'] == 2 and ticker['destino'] == 3:

                # ARS - BTC
                table_service.save_rates(EXCHANGE, 
                    ticker['dcb'], 
                    ticker['dca'], 
                    'ARS', 'BTC')
    except:
        logging.error(f'"{EXCHANGE}" scraping failed')