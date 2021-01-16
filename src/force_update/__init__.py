import logging
import azure.functions as func
from shared.version import current_version
from scrapers import run_all
from shared.cache import Cache

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Force update (v: {current_version})")

    run_all()

    # empty cache
    Cache.current_exchanges = []
    Cache.saved_time = None
    
    return func.HttpResponse(
        status_code=200
    )