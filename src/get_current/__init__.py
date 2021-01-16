import logging
import azure.functions as func
from shared.version import current_version
from shared import table_service
import json
from py_linq import Enumerable
from datetime import datetime
from shared.cache import Cache

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Get Current (v: {current_version})")

    if Cache.saved_time is not None:
        seconds_from_cache = (datetime.utcnow() - Cache.saved_time).total_seconds()
        modulo_seconds = (datetime.utcnow().minute % 10) * 60 + datetime.utcnow().second

    if len(Cache.current_exchanges) == 0 or Cache.saved_time is None or seconds_from_cache > modulo_seconds:

        data_source = 'database'

        entities = table_service.get_current()

        collection = Enumerable(entities).select(lambda x: { 
            'exchange': x['exchange'],
            'ticker': x['ticker'],
            'date': str(x['Timestamp'])[0:-6],
            'sell': x['sell'],
            'buy': x['buy'],
            'old': str(datetime.utcnow() - x['Timestamp'].replace(tzinfo=None))
        })

        exchangelist = collection.order_by(lambda x: x['ticker']).order_by(lambda x: x['sell']).to_list()

        Cache.current_exchanges = exchangelist
        Cache.saved_time = datetime.utcnow()
    else:
        print('Reading from cache')

        data_source = 'cache'

        exchangelist = Cache.current_exchanges
        
        for exchange in exchangelist:
            exchange['old'] = str(datetime.utcnow() - datetime.strptime(exchange['date'], '%Y-%m-%d %H:%M:%S.%f'))
            
    body = {
        'data': exchangelist,
        'version': current_version,
        'data-source': data_source
    }
    
    return func.HttpResponse(
        body=json.dumps(body),
        status_code=200,
        headers={
            "content-type": "application/json",
        }
    )
