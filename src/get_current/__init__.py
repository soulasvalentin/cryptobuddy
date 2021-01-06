import logging
import azure.functions as func
from shared.version import current_version
from shared import table_service
import json
from py_linq import Enumerable
from datetime import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Get Current (v: {current_version})")

    entities = table_service.get_current()

    collection = Enumerable(entities).select(lambda x: { 
        'exchange': x['RowKey'],
        'date': str(x['Timestamp']),
        'sell': x['sell'],
        'buy': x['buy'],
        'old': str(datetime.utcnow() - x['Timestamp'].replace(tzinfo=None))
    })

    body = json.dumps(collection.to_list())

    return func.HttpResponse(
        body=body,
        status_code=200,
        headers={
            "content-type": "application/json",
            "api-version": current_version
        }
    )
