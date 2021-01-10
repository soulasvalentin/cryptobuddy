import requests
from shared import table_service

EXCHANGE = 'ripio'

def scrap():    
    url = 'https://app.ripio.com/api/v3/public/rates/?country=AR'
    res = requests.get(url)
    obj = res.json()

    for ticker in obj:
        # ARS - BTC
        if ticker['ticker'] == 'BTC_ARS':
            table_service.save_rates(EXCHANGE, 
                float(ticker['sell_rate']), 
                float(ticker['buy_rate']), 
                'ARS', 'BTC')
        
        # ARS - ETH
        if ticker['ticker'] == 'ETH_ARS':
            table_service.save_rates(EXCHANGE, 
                float(ticker['sell_rate']), 
                float(ticker['buy_rate']), 
                'ARS', 'ETH')