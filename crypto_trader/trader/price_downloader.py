import time

from celery import shared_task, current_task
from celery.exceptions import Ignore
from django.conf import settings

from crypto_coinbase.coinbase import Coinbase
from crypto_trader.models import Currency
from crypto_trader.trader.trade_api import TradeAPI

trade_client: TradeAPI

if settings.TRADE_API == "coinbase":
    trade_client = Coinbase()


@shared_task
def download_prices_task(currency_id):
    currencies = [c.currency_id for c in Currency.objects.only("currency_id")]
    if currency_id not in currencies:
        current_task.update_state(state='FAILED', meta="Could not find currency %s" % currency_id)
        raise Ignore

    for i in range(10):
        current_task.update_state(state='PROGRESS', meta={'current': i, 'total': 10})
        time.sleep(1)
    print(trade_client)
