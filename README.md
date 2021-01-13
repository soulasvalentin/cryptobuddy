> ***Disclaimer**: This is a proof-of-concept project for Python serverless applications in Azure and Github Actions deployments. By no means we intend this app data to be used in any kind of production or real-life scenarios. At the same time, we do not declare ourselves as experts on the tackled subjects. Any kind of feedback is welcomed, issues are open.*

## Introduction

**CryptoBuddy** obtains cryptos *buy* & *sell* rates periodically and stores them to allow for market analysis. This is an **Azure Functions** project in Python. The scraper function is triggered with a CRON expression and retrieves and saves the data into a DB. A separate set of HTTP triggered functions will perform and return valuable analysis on the data when invoked.

At this stage, only **BTC-ARS** and **ETH-ARS** rates from Argentinean exchanges are supported.

#### Deploy Status

![deploy-src](https://github.com/soulasvalentin/cryptobuddy/workflows/deploy-src/badge.svg?branch=main)
![deploy-web](https://github.com/soulasvalentin/cryptobuddy/workflows/deploy-web/badge.svg)

## Usage

We offer a small (evergrowing) REST API set for consumption (see below). But at the same time, we expose the data through a simple website: [**CryptoBuddy**](https://tinyurl.com/cryptobuddy).

#### Available Endpoints

> Base URL: https://cryptobuddy.azurewebsites.net/api

- `GET /get_current` Returns the latest rates of every exchange

## Getting started

- Download and install Azure Function Core Tools version 3.x [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#install-the-azure-functions-core-tools).
- Instal VS Code extension: [Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
- Install Python 3.7
- Install Required Python modules:

```bash
pip install requests
pip install bs4
pip install azure-cosmosdb-table
pip install azure.functions
pip install py_linq
```

If you wish to debug locally, create the following **configuration file** in `src/locals.settings.json`

```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "SA_NAME": "<storage_account_table_name>",
    "SA_ACCOUNT_KEY": "<storage_account_key>"
  }
}
```

If you wish to deploy your own version, create a **StorageAccount** with the tables `current` and `history` and make sure that your Function App has the following environment variables configured:
- `SA_NAME`
- `SA_ACCOUNT_KEY`

## Testing

```bash
cd tests
python -m unittest discover -v
```

## Docs

- [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Work with Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cpython%2Cbash)
- [Getting started with Azure Table Storage API](https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python)

## Changelog

**v1.9.1** *(13JAN21)*

- **[WEB]** Fix: 'Old' column is not showing elapsed time
- **[SRC]** Fix: 'Get_current' endpoint is not returning 'old' from non-cached responses

**v1.9.0** *(12JAN21)*

- Add support for Github Actions (web & src)

**v1.8.0** *(11JAN21)*

- Fix: Satoshitango ETH scrap is failing
- Move scrapers run logic to scraper module
- Add endpoint for running the scraper on-demand (/force_update)
- Add basic web

**v1.7.1** *(11JAN21)*

- Fix: History data is not storing ticker information

**v1.7.0** *(10JAN21)*

- Store ticker origin and destination in DB
- Add support for ETH from current exchanges
- Get_current endpoint returns ETH as well as BTC rates
- Add error handling in scrapers

**v1.6.0** *(6JAN21)*

- Add cache support for exchange rates

**v1.5.2** *(6JAN21)*

- Fix: Some rates are being saved as string instead of double

**v1.5.1** *(6JAN21)*

- Fix: Modules references

**v1.5.0** *(5JAN21)*

- Add get_current endpoint

**v1.4.0** *(5JAN21)*

- Add Decrypto support

**v1.3.0** *(5JAN21)*

- Add Satoshitango support

**v1.2.1** *(5JAN21)*

- Fix environment variables names

**v1.2.0** *(5JAN21)*

- Add BuenBit support
- Add CryptoMarket support
- Add Ripio support

**v1.1.1** *(5JAN21)*

 - Init
