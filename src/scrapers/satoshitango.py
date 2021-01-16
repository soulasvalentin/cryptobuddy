import logging
import requests
from shared import table_service

EXCHANGE = 'satoshitango'
URL = 'https://api.satoshitango.com/v3/ticker/ARS'

def scrap():
    try:
        res = requests.get(URL)
        obj = res.json()

        # ARS - BTC
        table_service.save_rates(EXCHANGE, 
            obj['data']['ticker']['BTC']['bid'], 
            obj['data']['ticker']['BTC']['ask'], 
            'ARS', 'BTC')

        # ARS - ETH
        # table_service.save_rates(EXCHANGE, 
        #     obj['data']['ticker']['ETH']['bid'], 
        #     obj['data']['ticker']['ETH']['ask'], 
        #     'ARS', 'ETH')
    except:
        logging.error(f'"{EXCHANGE}" scraping failed')