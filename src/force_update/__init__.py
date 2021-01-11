import logging
import azure.functions as func
from shared.version import current_version
from scrapers import run_all

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Force update (v: {current_version})")

    run_all()
    
    return func.HttpResponse(
        status_code=200
    )