import requests
from shared import table_service

EXCHANGE = 'satoshitango'

def scrap():    
    url = 'https://api.satoshitango.com/v3/ticker/ARS'
    res = requests.get(url)
    obj = res.json()
    buy = obj['data']['ticker']['BTC']['bid']
    sell = obj['data']['ticker']['BTC']['ask']

    table_service.save_current(EXCHANGE, buy, sell)
    table_service.save_history(EXCHANGE, buy, sell)