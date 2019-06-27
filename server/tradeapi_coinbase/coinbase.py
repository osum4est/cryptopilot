from datetime import datetime

from cbpro import PublicClient

from server.api.models import Currency, Candle
from server.api.trader.trade_api import TradeAPI
from server.resources import cryptocurrency_icons


class Coinbase(TradeAPI):
    def __init__(self):
        self.public_client = PublicClient()

    def get_available_currencies(self):
        # TODO: Update currencies on server startup
        return [
            Currency(currency_id=product["id"], base_currency=product["base_currency"],
                     quote_currency=product["quote_currency"],
                     name=cryptocurrency_icons.get_currency_name(product["base_currency"]),
                     color=cryptocurrency_icons.get_currency_color(product["base_currency"]))
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
