import requests

EXCHANGE = 'letsbit'
URL = 'https://letsbit.io/api/v1/exchange/public/markets/tickers'

def scrap():
    tickers = []
       
    res = requests.get(URL)
    obj = res.json()

    # ARS - BTC
    tickers.append({
        'exchange': EXCHANGE,
        'ticker': 'ARS-BTC',
        'buy': round(float(obj['btcars']['ticker']['buy']), 2),
        'sell': round(float(obj['btcars']['ticker']['sell']), 2)
    })

    # USD - BTC
    tickers.append({
        'exchange': EXCHANGE,
        'ticker': 'USD-BTC',
        'buy': round(float(obj['btcusd']['ticker']['buy']), 2),
        'sell': round(float(obj['btcusd']['ticker']['sell']), 2)
    })

    return tickers