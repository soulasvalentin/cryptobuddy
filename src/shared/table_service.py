import logging
from datetime import datetime
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from shared.version import current_version
import os

table_name = os.environ["SA_NAME"]
table_account_key = os.environ["SA_ACCOUNT_KEY"]
table_service = TableService(account_name=table_name, account_key=table_account_key)

CURRENT_TABLENAME = 'current'
HISTORY_TABLENAME = 'history'

def save_current(exchange, buy, sell, origin, destination):
    logging.info("[table_service] saving as current..")

    entity = {
        'PartitionKey': exchange,
        'RowKey': f'{origin}-{destination}',
        'buy': buy, 
        'sell': sell
    }

    table_service.insert_or_merge_entity(CURRENT_TABLENAME, entity)

def save_history(exchange, buy, sell, origin, destination):
    logging.info("[table_service] saving as history..")

    entity = {
        'PartitionKey': exchange,
        'RowKey': str(datetime.utcnow()),
        'ticker': f'{origin}-{destination}',
        'buy': buy, 
        'sell': sell,
        'v': current_version
    }

    table_service.insert_or_merge_entity(HISTORY_TABLENAME, entity)

def save_rates(exchange, buy, sell, origin, destination):
    logging.info(f"[table_service] saving rates.. (exchange={exchange}, buy={buy}, sell={sell}, origin={origin}, destination={destination})")
    save_current(exchange, buy, sell, origin, destination)
    save_history(exchange, buy, sell, origin, destination)

def get_current():
    logging.info("[table_service] get current..")

    entities = table_service.query_entities(CURRENT_TABLENAME)

    return entities.items
