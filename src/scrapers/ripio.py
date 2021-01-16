import logging
import requests
from shared import table_service

EXCHANGE = 'ripio'
URL = 'https://app.ripio.com/api/v3/public/rates/?country=AR'

def scrap():   
    try: 
        res = requests.get(URL)
        obj = res.json()

        for ticker in obj:
            # ARS - BTC
            if ticker['ticker'] == 'BTC_ARS':
                table_service.save_rates(EXCHANGE, 
                    float(ticker['sell_rate']), 
                    float(ticker['buy_rate']), 
                    'ARS', 'BTC')
            
            # ARS - ETH
            # if ticker['ticker'] == 'ETH_ARS':
            #     table_service.save_rates(EXCHANGE, 
            #         float(ticker['sell_rate']), 
            #         float(ticker['buy_rate']), 
            #         'ARS', 'ETH')
    except:
        logging.error(f'"{EXCHANGE}" scraping failed')