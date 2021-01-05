import azure.functions as func
import logging
from scrapers import letsbit
from shared.version import current_version

def main(mytimer: func.TimerRequest) -> None:
    logging.info(f"Scraper started (v: {current_version})")

    letsbit.scrap()
