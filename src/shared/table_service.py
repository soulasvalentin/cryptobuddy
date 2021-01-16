from azure.cosmosdb.table.tableservice import TableService, TableBatch
from azure.cosmosdb.table.models import Entity
import os

table_name = os.environ["SA_NAME"]
table_account_key = os.environ["SA_ACCOUNT_KEY"]
table_service = TableService(account_name=table_name, account_key=table_account_key)

CURRENT_TABLENAME = 'current'
HISTORY_TABLENAME = 'history'

def save_current(partial_entities):
    batch = TableBatch()

    for partial_entity in partial_entities:
        entity = {
            'PartitionKey': 'current',
            'RowKey': f"{partial_entity['exchange']}-{partial_entity['ticker']}",
            'exchange': partial_entity['exchange'], 
            'ticker': partial_entity['ticker'], 
            'buy': partial_entity['buy'], 
            'sell': partial_entity['sell']
        }
        batch.insert_or_merge_entity(entity)

    table_service.commit_batch(CURRENT_TABLENAME, batch)

def get_current():
    entities = table_service.query_entities(CURRENT_TABLENAME)
    return entities.items
