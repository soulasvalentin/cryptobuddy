import logging
import requests
from shared import table_service

EXCHANGE = 'buenbit'
URL = 'https://be.buenbit.com/api/market/tickers/'

def scrap():  
    try:  
        res = requests.get(URL)
        obj = res.json()

        # ARS - BTC
        table_service.save_rates(EXCHANGE, 
            float(obj['object']['btcars']['purchase_price']), 
            float(obj['object']['btcars']['selling_price']), 
            'ARS', 'BTC')
    except:
        logging.error(f'"{EXCHANGE}" scraping failed')