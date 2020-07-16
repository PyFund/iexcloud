import pandas as pd
import requests
import json

from typing import Union, List
from requests import Response
from iexcloud.config import get_token, get_url


class Stock(object):
    def __init__(self, symbol: str, output="pandas"):

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

    def _create_output(self, response: Response, attribute: str = None):

        if response:

            if self.output == "json":
                return response.text
            elif self.output == "pandas":
                return self._response_text_to_pd(response.text, attribute)

        else:  # pragma: no cover
            raise response.raise_for_status()

    def _response_text_to_pd(self, response_text: str, attribute: str = None):

        response_text = response_text.replace("'", '"')

        if attribute is not None:
            response_text = json.loads(response_text)[attribute]
            response_text = json.dumps(response_text)

        return pd.read_json(response_text)

    def get_dividend(self, time_range: str) -> Union[pd.DataFrame, str]:
        """basic dividend data for US equities, ETFs, and Mutual Funds.

        Args:
            time_range: time range to retrieve dividend for. Options are:

                - 5y: Five years
                - 2y: Two years
                - 1y: One year
                - ytd: Year-to-date
                - 6m: Six months
                - 3m: Three months
                - 1m: One month
                - next: The next upcoming dividend

        Returns:
            pd.DataFrame or JSON str: Dividend information with following fields

                - exDate( (string) )refers to the dividend ex-date
                - paymentDate( (string) )refers to the payment date
                - recordDate( (string) )refers to the dividend record date
                - declaredDate( (string) )refers to the dividend declaration date
                - amount (number) refers to the payment amount
                - flag( (string) )Type of dividend event
                - currency( (string) )Currency of the dividend
                - description( (string) )Description of the dividend event
                - frequency( (string) )Frequency of the dividend
        """

        api_url = f"{get_url()}/stock/{self.symbol}/dividends/{time_range}?"
        response = requests.get(api_url, params={"token": get_token()})
        output = self._create_output(response)

        self.dividend = output

        return output

    def get_earning(self, last: int) -> Union[pd.DataFrame, str]:
        """Earnings data for a given company including the actual EPS and other info.

        Args:
            last: Number of quarters or years to return.

        Returns:
            pd.DataFrame or JSON str: Earnings information with following fields
                - actualEPS (number) Actual earnings per share for the period.
                    EPS data is split-adjusted by default. Earnings data accounts
                    for all corporate actions including dilutions, splits, reverse
                    splits, spin-offs, exceptional dividends, and rights issues.
                - consensusEPS (number) Consensus EPS estimate trend for the period
                - announceTime (string) Time of earnings announcement.
                    BTO (Before open), DMT (During trading), AMC (After close)
                - numberOfEstimates (number) Number of estimates for the period
                - EPSSurpriseDollar (number) Dollar amount of EPS surprise for the
                    period
                - EPSReportDate (string) Expected earnings report date YYYY-MM-DD
                - fiscalPeriod (string) The fiscal quarter Q# YYYY or the fiscal year
                    FY ending in YYYY the earnings data applies to
                - fiscalEndDate (string) Date representing the company fiscal quarter
                    end YYYY-MM-DD
                - yearAgo (number) Represents the EPS of the quarter a year ago
                - yearAgoChangePercent (number) Represents the percent difference
                    between the quarter a year ago actualEPS and current period
                    actualEPS.
        """

        api_url = f"{get_url()}/stock/{self.symbol}/earnings/{last}?"
        response = requests.get(api_url, params={"token": get_token()})
        output = self._create_output(response, "earnings")

        self.earning = output

        return output

    def get_logo(self) -> str:
        """Load url to company logo

        Returns:
            str: Load url to company logo
        """

        api_url = f"{get_url()}/stock/{self.symbol}/logo?"
        response = requests.get(api_url, params={"token": get_token()})
        output = json.loads(response.text)["url"]

        self.logo = output

        return output

    def get_news(self, last: int) -> Union[pd.DataFrame, str]:
        """Provides intraday news from over 3,000 global news sources

        Args:
            last: Number of news to return. Between 1 and 50.

        Returns:
            pd.DataFrame or JSON str: news information with following fields

                - datetime (number) Millisecond epoch of time of article
                - headline (string)
                - source (string) Source of the news article. Make sure to
                    always attribute the source.
                - url (string) URL to IEX Cloud for associated news image.
                    Note: You will need to append your token before calling.
                - summary (string)
                - related (string) Comma-delimited list of tickers associated
                    with this news article. Not all tickers are available on the API.
                    Make sure to check against available ref-data
                - image (string) URL to IEX Cloud for associated news image.
                    Note: You will need to append your token before calling.
                - lang (string) Language of the source article
                - hasPaywall (boolean) Whether the news source has a paywall
        """
        api_url = f"{get_url()}/stock/{self.symbol}/news/last/{last}"
        response = requests.get(api_url, params={"token": get_token()})
        output = self._create_output(response)

        self.news = output

        return output

    def get_peer(self) -> List[str]:
        """Get peer group of stock

        Returns:
            List[str]: list of peers
        """

        api_url = f"{get_url()}/stock/{self.symbol}/peers"
        response = requests.get(api_url, params={"token": get_token()})
        output = json.loads(response.text)

        self.peer = output

        return output

    def get_price(self, time_range: str) -> Union[pd.DataFrame, str]:
        """Returns adjusted and unadjusted historical data for up to 15 years.

        Args:
            time_range:
                - max: All available data up to 15 years
                - 5y: Five years
                - 2y: Two yearskkj
                - 1y: One year
                - ytd: Year-to-date
                - 6m: Six months
                - 3m: Three months
                - 1m: One month (default)
                - 1mm: One month in 30 minute intervals
                - 5d: Five Days by day.
                - 5dm: Five Days in 10 minute intervals

        Returns:
            pd.DataFrame or JSON str: Historical price information with following fields
                - date: ( (string) ) Formatted as YYYY-MM-DD
                - high: (number) Adjusted data for historical dates.
                    Split adjusted only.
                - low: (number) Adjusted data for historical dates.
                    Split adjusted only.
                - volume: (number) Adjusted data for historical dates.
                    Split adjusted only.
                - open: (number) Adjusted data for historical dates.
                    Split adjusted only.
                - close: (number) Adjusted data for historical dates.
                    Split adjusted only.
                - uHigh: (number) Unadjusted data for historical dates.
                - uLow: (number) Unadjusted data for historical dates.
                - uVolume: (number) Unadjusted data for historical dates.
                - uOpen: (number) Unadjusted data for historical dates.
                - uClose: (number) Unadjusted data for historical dates.
                - changeOverTime: (number) Percent change of each interval relative
                    to first value. Useful for comparing multiple stocks.
                - label: (number) A human readable format of the date depending on
                    the range.
                - change: (number) Change from previous trading day.
                - changePercent: (number) Change percent from previous trading day.
        """

        api_url = f"{get_url()}/stock/{self.symbol}/chart/{time_range}"
        response = requests.get(api_url, params={"token": get_token()})
        output = self._create_output(response)

        self.price = output

        return output

    def get_profile(self) -> dict:
        """get company profile

        Returns:
            Dictionary with the following fields:
                symbol (string)
                companyName (string) Name of the company
                employees (number) Number of employees
                exchange (string)
                industry (string)
                website (string)
                description (string)
                CEO (string)
                securityName (string) Name of the security
                issueType (string) refers to the common issue type of the stock.
                    ad – American Depository Receipt (ADR’s)
                    re – Real Estate Investment Trust (REIT’s)
                    ce – Closed end fund (Stock and Bond Fund)
                    si – Secondary Issue
                    lp – Limited Partnerships
                    cs – Common Stock
                    et – Exchange Traded Fund (ETF)
                    wt – Warrant
                    rt – Right
                    (blank) – Not Available, i.e., Note, or (non-filing)
                      Closed Ended Funds
                    ut - Unit
                    temp - Temporary
                sector (string)
                primarySicCode (string) Primary SIC Code for the symbol (if available)
                tags (array) an array of strings used to classify the company.
                address (string) street address of the company if available
                address2 (string) street address of the company if available
                state (string) state of the company if available
                city (string) city of the company if available
                zip (string) zip of the company if available
                country (string) country of the company if available
                phone (string) phone number of the company if available
        """

        api_url = f"{get_url()}/stock/{self.symbol}/company"
        response = requests.get(api_url, params={"token": get_token()})
        output = json.loads(response.text)

        self.profile = output

        return output

    def get_split(self, time_range: str) -> Union[pd.DataFrame, str]:
        """get stock splits

        Args:
            time_range: time range to retrieve dividend for. Options are:

                - 5y: Five years
                - 2y: Two years
                - 1y: One year
                - ytd: Year-to-date
                - 6m: Six months
                - 3m: Three months
                - 1m: One month
                - next: The next upcoming dividend

        Returns:
            pd.DataFrame or JSON str: news information with following fields

                - exDate (string) refers to the split ex-date
                - declaredDate (string) refers to the split declaration date
                - ratio (number) refers to the split ratio. The split ratio is an
                    inverse of the number of shares that a holder of the stock
                    would have after the split divided by the number of shares
                    that the holder had before.
                    For example: Split ratio of .5 = 2 for 1 split.
                - toFactor (string) To factor of the split. Used to calculate the
                    split ratio fromfactor/tofactor = ratio (eg ½ = 0.5)
                - fromFactor (string) From factor of the split. Used to calculate
                    the split ratio fromfactor/tofactor = ratio (eg ½ = 0.5)
                - description (string) Description of the split event.
        """

        api_url = f"{get_url()}/stock/{self.symbol}/splits/{time_range}"
        response = requests.get(api_url, params={"token": get_token()})

        output = self._create_output(response)

        self.split = output

        return output
