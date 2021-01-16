import requests

EXCHANGE = 'ripio'
URL = 'https://app.ripio.com/api/v3/public/rates/?country=AR'

def scrap():   
    tickers = []
       
    res = requests.get(URL)
    obj = res.json()

    for ticker in obj:
        # ARS - BTC
        if ticker['ticker'] == 'BTC_ARS':
            tickers.append({
                'exchange': EXCHANGE,
                'ticker': 'ARS-BTC',
                'buy': round(float(ticker['sell_rate']), 2),
                'sell': round(float(ticker['buy_rate']), 2)
            })

    return tickers
