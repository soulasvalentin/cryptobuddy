import requests

EXCHANGE = 'cryptomkt'
URL = 'https://api.cryptomkt.com/v1/ticker'

def scrap():   
    tickers = [] 
    
    res = requests.get(URL)
    obj = res.json()

    for ticker in obj['data']:
        # ARS - BTC
        if ticker['market'] == 'BTCARS':            
            tickers.append({
                'exchange': EXCHANGE,
                'ticker': 'ARS-BTC',
                'buy': round(float(ticker['bid']), 2),
                'sell': round(float(ticker['ask']), 2)
            })

    return tickers
