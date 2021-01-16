import requests

EXCHANGE = 'satoshitango'
URL = 'https://api.satoshitango.com/v3/ticker/ARS'

def scrap():
    tickers = []
    
    res = requests.get(URL)
    obj = res.json()

    # ARS - BTC
    tickers.append({
        'exchange': EXCHANGE,
        'ticker': 'ARS-BTC',
        'buy': round(obj['data']['ticker']['BTC']['bid'], 2),
        'sell': round(obj['data']['ticker']['BTC']['ask'], 2)
    })

    return tickers