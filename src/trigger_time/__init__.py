import azure.functions as func
import logging
from shared.version import current_version
from scrapers import letsbit, buenbit, cryptomkt, ripio, satoshitango, decrypto

def main(mytimer: func.TimerRequest) -> None:
    logging.info(f"Scraper started (v: {current_version})")

    letsbit.scrap()
    buenbit.scrap()
    cryptomkt.scrap()
    ripio.scrap()
    satoshitango.scrap()
    decrypto.scrap()
