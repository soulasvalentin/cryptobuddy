import requests

EXCHANGE = 'decrypto'
URL = 'https://api.decrypto.com.ar:8081/1.0/frontend/precios/'

def scrap(): 
    tickers = []

    res = requests.get(URL)
    obj = res.json()

    for ticker in obj['data']:
        # ARS - BTC
        if ticker['origen'] == 2 and ticker['destino'] == 3:
            tickers.append({
                'exchange': EXCHANGE,
                'ticker': 'ARS-BTC',
                'buy': round(ticker['dcb'], 2),
                'sell': round(ticker['dca'], 2)
            })

        # USD - BTC
        if ticker['origen'] == 1 and ticker['destino'] == 3:
            tickers.append({
                'exchange': EXCHANGE,
                'ticker': 'USD-BTC',
                'buy': round(ticker['dcb'], 2),
                'sell': round(ticker['dca'], 2)
            })    

    return tickers