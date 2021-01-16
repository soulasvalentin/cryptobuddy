import requests

EXCHANGE = 'buenbit'
URL = 'https://be.buenbit.com/api/market/tickers/'

def scrap():  
    tickers = []
       
    res = requests.get(URL)
    obj = res.json()

    # ARS - BTC
    tickers.append({
        'exchange': EXCHANGE,
        'ticker': 'ARS-BTC',
        'buy': round(float(obj['object']['btcars']['purchase_price']), 2),
        'sell': round(float(obj['object']['btcars']['selling_price']), 2)
    })

    return tickers