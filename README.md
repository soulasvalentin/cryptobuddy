## Introduction

**CryptoBuddy** obtains cryptos *buy* & *sell* rates periodically and stores them to allow for market analysis. This is an **Azure Functions** project in Python. The function is triggered with a CRON expresion and retrieves and saves the data. A separate set of HTTP triggered functions will perform and return valuable analysis on the data when invoked.

At this stage, only **BTC-ARS** rates from Argentinean exchanges are supported.

## Getting started

- Download and install Azure Function Core Tools version 3.x [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#install-the-azure-functions-core-tools).
- Instal VS Code extension: [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
- Install Python 3.7
- Install Required Python modules:

```bash
pip install requests
pip install bs4
pip install azure-cosmosdb-table
```

If you wish to debug locally, create the following **configuration file** in `src/locals.settings.json`

```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "TABLE_ACCOUNT_KEY": "<storage_account_key>",
    "TABLE_NAME": "<storage_account_table_name>"
  }
}
```

If you wish to deploy your own version, create a **StorageAccount** with the tables `current` and `history` and make sure that your Function App has the following environment variables configured:
- `TABLE_ACCOUNT_KEY`
- `TABLE_NAME`

## Docs

- [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Work with Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cpython%2Cbash)

## Changelog

**v1.2.0** *(5JAN21)*

- Added BuenBit scraper
- Added CryptoMarket scraper
- Added Ripio scraper

**v1.1.1** *(5JAN21)*

 - Init