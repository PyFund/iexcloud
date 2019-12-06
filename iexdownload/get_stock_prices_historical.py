import requests

from iexdownload.constants import *


def get_stock_prices_historical(symbol: str, range: str):

    api_query = f"{IEX_CLOUD}/stock/{symbol}/chart/{range}?token={IEX_TOKEN}"
    print(api_query)
    return requests.get(api_query).json()


print(get_stock_prices_historical("TWTR", "5d"))

