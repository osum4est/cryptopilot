from django.db import models


class Currency(models.Model):
    currency_id = models.CharField(max_length=16, unique=True)
    base_currency = models.CharField(max_length=16)
    quote_currency = models.CharField(max_length=16)


class Candle(models.Model):
    currency = models.ForeignKey(Currency, to_field="currency_id", on_delete=models.PROTECT)
    granularity = models.IntegerField()
    time = models.DateTimeField()
    low = models.DecimalField(max_digits=12, decimal_places=2)
    high = models.DecimalField(max_digits=12, decimal_places=2)
    open = models.DecimalField(max_digits=12, decimal_places=2)
    close = models.DecimalField(max_digits=12, decimal_places=2)
    volume = models.DecimalField(max_digits=12, decimal_places=2)


class TradeSession(models.Model):
    # TODO: Support taking savings out
    start_amount = models.DecimalField(max_digits=12, decimal_places=2)
    start_time = models.DateTimeField()
    end_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    end_time = models.DateTimeField(null=True)
    simulation = models.BooleanField()
    active = models.BooleanField()
    creator = models.CharField(max_length=256)


class Trade(models.Model):
    currency = models.ForeignKey(Currency, to_field="currency_id", on_delete=models.PROTECT)
    trader = models.CharField(max_length=256)
    session = models.ForeignKey(TradeSession, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=8)  # TODO: Is this too many/little?
    price = models.DecimalField(max_digits=12, decimal_places=2)
    time = models.DateTimeField()
    notes = models.CharField(max_length=1024)
