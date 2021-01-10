import requests
from shared import table_service

EXCHANGE = 'ripio'

def scrap():    
    url = 'https://app.ripio.com/api/v3/public/rates/?country=AR'
    res = requests.get(url)
    tickers = res.json()
    for ticker in tickers:
        if ticker['ticker'] == 'BTC_ARS':
            buy = float(ticker['sell_rate'])
            sell = float(ticker['buy_rate'])

            table_service.save_current(EXCHANGE, buy, sell, 'ARS', 'BTC')
            table_service.save_history(EXCHANGE, buy, sell, 'ARS', 'BTC')