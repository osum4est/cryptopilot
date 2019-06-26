from datetime import datetime

from cbpro import PublicClient

from server.api.models import Currency, Candle
from server.api.trader.trade_api import TradeAPI


class Coinbase(TradeAPI):
    def __init__(self):
        self.public_client = PublicClient()

    def get_available_currencies(self):
        # TODO: Update currencies on server startup
        # TODO: Use cryptocurrency-icons manifest.json for names and colors
        currency_details = self.public_client.get_currencies()
        return [
            Currency(currency_id=product["id"], base_currency=product["base_currency"],
                     quote_currency=product["quote_currency"],
                     name=next(c["name"] for c in currency_details if c["id"] == product["base_currency"]))
            for product in self.public_client.get_products()
        ]

    def get_historic_rates(self, currency_id, start_date, end_date, granularity):
        return [
            Candle(currency_id=currency_id, granularity=granularity, time=datetime.utcfromtimestamp(candle[0]),
                   low=candle[1], high=candle[2], open=candle[3], close=candle[4],
                   volume=candle[5])
            for candle in
            self.public_client.get_product_historic_rates(currency_id, start_date.isoformat(), end_date.isoformat(),
                                                          granularity)
        ]
        pass
