import requests

from iexcloud.constants import IEX_CLOUD, IEX_TOKEN


class Stock(object):

    def __init__(self, symbol: str):
        self.symbol = symbol

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

        if response:
            return response.json()

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

        if response:
            return response.json()

    def get_logo(self):
        """https://iexcloud.io/docs/api/#logo

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/logo?"
        response = requests.get(api_url, params={'token': IEX_TOKEN})

        if response:
            return response.json()

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

        if response:
            return response.json()

    def get_peer(self):
        """https://iexcloud.io/docs/api/#peer-groups

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/peers"
        response = requests.get(api_url, params={'token': IEX_TOKEN})

        if response:
            return response.json()

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

        if response:
            return response.json()

    def get_profile(self):
        """https://iexcloud.io/docs/api/#company

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/stock/{self.symbol}/company"
        response = requests.get(api_url, params={'token': IEX_TOKEN})

        if response:
            return response.json()

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

        if response:
            return response.json()

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

        if response:
            return response.json()
