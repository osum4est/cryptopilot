from cbpro import PublicClient

from crypto_trader.models import Currency
from crypto_trader.trader.trade_api import TradeAPI


class Coinbase(TradeAPI):
    def __init__(self):
        self.public_client = PublicClient()

    def get_available_currencies(self):
        return [
            Currency(currency_id=product["id"], base_currency=product["base_currency"],
                     quote_currency=product["quote_currency"]) for product in self.public_client.get_products()
        ]
