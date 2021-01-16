import logging
import requests
from shared import table_service

EXCHANGE = 'letsbit'
URL = 'https://letsbit.io/api/v1/exchange/public/markets/tickers'

def scrap():
    try:    
        res = requests.get(URL)
        obj = res.json()

        # ARS - BTC
        table_service.save_rates(EXCHANGE, 
            float(obj['btcars']['ticker']['buy']), 
            float(obj['btcars']['ticker']['sell']), 
            'ARS', 'BTC')

        # ARS - ETH
        # table_service.save_rates(EXCHANGE, 
        #     float(obj['ethars']['ticker']['buy']), 
        #     float(obj['ethars']['ticker']['sell']), 
        #     'ARS', 'ETH')

        # USD - BTC
        table_service.save_rates(EXCHANGE, 
            float(obj['btcusd']['ticker']['buy']), 
            float(obj['btcusd']['ticker']['sell']), 
            'USD', 'BTC')
    except:
        logging.error(f'"{EXCHANGE}" scraping failed')