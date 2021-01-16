import logging
from shared.version import current_version
from shared import table_service
from scrapers import letsbit, buenbit, cryptomkt, ripio, satoshitango, decrypto

def run_all():
    logging.info(f"[scraper] running all scrapers.. (v: {current_version})")

    scrapers = [
        letsbit,
        buenbit,
        cryptomkt,
        ripio,
        satoshitango,
        decrypto
    ]

    alltickers = []

    # run scrapers sequentially up to 3 attempts each
    for scraper in scrapers:
        logging.info(f"[scraper/{scraper.EXCHANGE}] started..")
        attempts = 1
        while attempts <= 3:
            logging.info(f"[scraper/{scraper.EXCHANGE}] attempt #{attempts}")
            try:
                # run scraper
                tickers = scraper.scrap()
                logging.info(f"[scraper/{scraper.EXCHANGE}] tickers={tickers}")

                # append data to pool
                alltickers.extend(tickers)

                break
            except:
                attempts += 1

        logging.info(f"[scraper/{scraper.EXCHANGE}] done")

    logging.info(f'[scraper] scraping done. {len(alltickers)} tickers scraped from {len(scrapers)} exchanges')

    logging.info('[scraper] storing in db..')
    table_service.save_current(alltickers)

    logging.info('[scraper] done')