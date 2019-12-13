from typing import List
import requests

from iexcloud.constants import IEX_CLOUD, IEX_TOKEN


class Reference(object):

    def __init__(self):

        self.msg_limit: int = self.get_msg_limit()
        self.msg_used: int = self.get_msg_used()
        self.msg_balance: int = self.msg_limit - self.msg_used
        self.symbols: List[str] = self.get_symbols()

    @staticmethod
    def get_msg_limit() -> int:
        """https://iexcloud.io/docs/api/#metadata

        Parameters
        ----------

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/account/metadata?token={IEX_TOKEN}"
        response = requests.get(api_url)

        if response:
            return response.json()['messageLimit']

    @staticmethod
    def get_msg_used() -> int:
        """https://iexcloud.io/docs/api/#metadata

        Parameters
        ----------

        Returns
        -------

        """

        api_url = f"{IEX_CLOUD}/account/metadata?token={IEX_TOKEN}"
        response = requests.get(api_url)

        if response:
            return response.json()['messagesUsed']

    @staticmethod
    def get_symbols():

        api_url = f"{IEX_CLOUD}/ref-data/iex/symbols?token={IEX_TOKEN}"
        response = requests.get(api_url)

        if response:
            return [symbol['symbol'] for symbol in response.json()]

    def update_msg_limit(self):

        self.msg_limit = self.get_msg_limit()

    def update_msg_used(self):

        self.msg_used = self.get_msg_used()

    def update_msg_balance(self):

        self.msg_limit = self.get_msg_limit()
        self.msg_used = self.get_msg_used()
        self.msg_balance = self.msg_limit - self.msg_usess
