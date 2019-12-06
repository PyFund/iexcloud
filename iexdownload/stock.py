import requests

from iexdownload.constants import *


def get_historical_price(symbol: str, range: str):

    api_query = f"{IEX_CLOUD}/stock/{symbol}/chart/{range}?token={IEX_TOKEN}"
    print(api_query)
    return requests.get(api_query).json()
