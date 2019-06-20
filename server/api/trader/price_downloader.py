from datetime import datetime, timedelta

from celery import shared_task, current_task
from celery.exceptions import Ignore
from django.conf import settings

from server.tradeapi_coinbase.coinbase import Coinbase
from server.api.models import Currency, Candle
from server.api.trader.trade_api import TradeAPI

trade_client: TradeAPI

if settings.TRADE_API == "coinbase":
    trade_client = Coinbase()


@shared_task
def download_prices_task(currency_id):
    currencies = [c.currency_id for c in Currency.objects.only("currency_id")]
    if currency_id not in currencies:
        current_task.update_state(state='FAILED', meta="Could not find currency %s" % currency_id)
        raise Ignore

    # days = 365 * 2
    days = 14
    granularity = 60
    prices_per_call = 300
    time_per_call = timedelta(minutes=int(granularity / 60) * prices_per_call)

    try:
        start_date = Candle.objects.filter(currency_id=currency_id, granularity=granularity).latest("time").time
    except Candle.DoesNotExist:
        start_date = datetime.utcnow() - timedelta(days=days)
    final_date = datetime.utcnow()
    end_date = start_date + time_per_call

    current_call = 0
    total_calls = int(((final_date - start_date).days * 24 * 60) / 300)

    while start_date < final_date:
        for candle in trade_client.get_historic_rates(currency_id, start_date, end_date, granularity):
            candle.save()
        start_date += time_per_call
        end_date += time_per_call
        current_task.update_state(state='PROGRESS', meta={'current': current_call, 'total': total_calls})
        current_call += 1

    print(trade_client)
