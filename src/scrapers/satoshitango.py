import requests
from shared import table_service

EXCHANGE = 'satoshitango'

def scrap():    
    url = 'https://api.satoshitango.com/v3/ticker/ARS'
    res = requests.get(url)
    obj = res.json()

    # ARS - BTC
    table_service.save_rates(EXCHANGE, 
        obj['data']['ticker']['BTC']['bid'], 
        obj['data']['ticker']['BTC']['ask'], 
        'ARS', 'BTC')

    # ARS - ETH
    table_service.save_rates(EXCHANGE, 
        obj['data']['ticker']['ETH']['bid'], 
        obj['data']['ticker']['ETH']['ask'], 
        'ARS', 'BTC')