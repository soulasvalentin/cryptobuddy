import requests
from datetime import datetime
from bs4 import BeautifulSoup
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

table_service = TableService(account_name='cryptobuddy', account_key='XQotXuwaI3nI25dUisUsTsw0uCzs73NLFit21BEOPSN+MWLIVQqnxGy6cSSHz6vvibPARr0b2Nri2pAbU0Eotg==')

def appendValue(exch, buy, sell):
    print(f"    buy={buy} sell={sell}")

    # upsert current data
    print("    saving as current..")
    current = {'PartitionKey': 'current_price', 'RowKey': exch,
        'buy': buy, 'sell': sell}
    table_service.insert_or_merge_entity('current', current)

    # insert history data
    print("    saving as history..")
    history = {'PartitionKey': exch, 'RowKey': str(datetime.now()),
        'buy': buy, 'sell': sell}
    table_service.insert_entity('history', history)

    print("    done")

print("Scraper started")

print("  let's bit..")
try:
    url = 'https://letsbit.io/api/v1/exchange/public/markets/tickers'
    res = requests.get(url)
    obj = res.json()
    buy = obj['btcars']['ticker']['buy']
    sell = obj['btcars']['ticker']['sell']
    appendValue('letsbit', buy, sell)
except:
    pass