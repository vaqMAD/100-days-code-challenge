import requests
import credentials


API_KEY = credentials.ALPHA_VANTAGE_API
API_ENDPOINT = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED'

PARAMS = {
    "symbol": "TSLA",
    "apikey": {API_KEY}
}


class StockData():

    def __init__(self) -> None:
        self.data = self._get_data_from_api()

        self.time_series = self.data["Time Series (Daily)"]
        self.time_series_list = [value for (
            key, value) in self.time_series.items()]
        self.yesterday = self.time_series_list[0]
        self.before_yesterday = self.time_series_list[1]

        self.stock_price_yesterday = float(self.yesterday["4. close"])
        self.stock_price_before_yesterday = float(
            self.before_yesterday["4. close"])

        self.percentage_stock_value_difference = self._get_difference_percentage_stock_value()

        self.is_difference_significant = self.check_difference_percentage_stock_value()

    def _get_data_from_api(self) -> dict:

        r = requests.get(url=API_ENDPOINT, params=PARAMS)
        r.raise_for_status()
        return r.json()

    def _get_difference_percentage_stock_value(self) -> float:

        difference = self.stock_price_yesterday - self.stock_price_before_yesterday
        return difference * 100 / self.stock_price_yesterday

    def check_difference_percentage_stock_value(self) -> bool:
        if self.percentage_stock_value_difference > 0.5 or self.percentage_stock_value_difference < -0.5:
            return True
        else:
            return False
