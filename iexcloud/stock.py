import time

import pandas as pd
import requests
from requests import Response

from iexcloud.constants import IEX_CLOUD, IEX_TOKEN


class Stock(object):

    def __init__(self, symbol: str, output="json"):

        self.symbol: str = symbol
        self.output: str = output
        self.dividend = None
        self.earning = None
        self.logo = None
        self.news = None
        self.peer = None
        self.price = None
        self.profile = None
        self.sentiment = None
        self.split = None

    def _response_text_to_pd(self, response_text: str):

        response_text = response_text.replace("'", '"')

        if not response_text.startswith("[") and not response_text.endswith("]"):
            response_text = "[" + response_text + "]"

        df = pd.read_json(response_text)
        df['symbol'] = self.symbol
        df['retrieved'] = time.time()

        return df

    def _create_output(self, response: Response):

        if response:
            cases = {
                "json": response.text,
                "pandas": self._response_text_to_pd(response.text)
            }
            return cases[self.output]
        else:
            raise response.raise_for_status()

    def get_dividend(self, time_range: str):
        """https://iexcloud.io/docs/api/#dividends-basic

        Parameters
        ----------
        time_range: str

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/dividends/{time_range}?"
        response = requests.get(api_url, params={'token': IEX_TOKEN})
        output = self._create_output(response)

        self.dividend = output

        return output

    def get_earning(self, last: int):
        """https://iexcloud.io/docs/api/#earnings

        Parameters
        ----------
        last: int

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/earnings/{last}?"
        response = requests.get(api_url, params={'token': IEX_TOKEN})
        output = self._create_output(response)

        self.earning = output

        return output

    def get_logo(self):
        """https://iexcloud.io/docs/api/#logo

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/logo?"
        response = requests.get(api_url, params={'token': IEX_TOKEN})
        output = self._create_output(response)

        self.logo = output

        return output

    def get_news(self, last: int):
        """https://iexcloud.io/docs/api/#news

        Parameters
        ----------
        last

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/news/last/{last}"
        response = requests.get(api_url, params={'token': IEX_TOKEN})
        output = self._create_output(response)

        self.news = output

        return output

    def get_peer(self):
        """https://iexcloud.io/docs/api/#peer-groups

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/peers"
        response = requests.get(api_url, params={'token': IEX_TOKEN})
        output = self._create_output(response)

        self.peer = output

        return output

    def get_price(self, time_range: str):
        """
        https://iexcloud.io/docs/api/#historical-prices

        Parameters
        ----------
        time_range

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/chart/{time_range}"
        response = requests.get(api_url, params={'token': IEX_TOKEN})
        output = self._create_output(response)

        self.price = output

        return output

    def get_profile(self):
        """https://iexcloud.io/docs/api/#company

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/company"
        response = requests.get(api_url, params={'token': IEX_TOKEN})
        output = self._create_output(response)

        self.profile = output

        return output

    def get_sentiment(self, date):
        """https://iexcloud.io/docs/api/#social-sentiment

        Parameters
        ----------
        date

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/sentiment/mute/{date}"
        response = requests.get(api_url, params={'token': IEX_TOKEN})

        output = self._create_output(response)

        self.sentiment = output

        return output

    def get_split(self, time_range: str):
        """https://iexcloud.io/docs/api/#splits-basic

        Parameters
        ----------
        time_range

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/splits/{time_range}"
        response = requests.get(api_url, params={'token': IEX_TOKEN})

        output = self._create_output(response)

        self.split = output

        return output
