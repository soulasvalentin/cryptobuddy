import logging
import requests
from shared import table_service

EXCHANGE = 'cryptomkt'
URL = 'https://api.cryptomkt.com/v1/ticker'

def scrap():    
    try:
        res = requests.get(URL)
        obj = res.json()

        for ticker in obj['data']:
            # ARS - BTC
            if ticker['market'] == 'BTCARS':            
                table_service.save_rates(EXCHANGE, 
                    float(ticker['bid']), 
                    float(ticker['ask']), 
                    'ARS', 'BTC')

            # ARS - ETH
            # if ticker['market'] == 'ETHARS':            
            #     table_service.save_rates(EXCHANGE, 
            #         float(ticker['bid']), 
            #         float(ticker['ask']), 
            #         'ARS', 'ETH')
    except:
        logging.error(f'"{EXCHANGE}" scraping failed')