from django.db import models


class Currency(models.Model):
    currency_id = models.CharField(max_length=16, unique=True, null=False)
    base_currency = models.CharField(max_length=16, null=False)
    quote_currency = models.CharField(max_length=16, null=False)


class Candle(models.Model):
    currency_id = models.ForeignKey(Currency, to_field="currency_id", on_delete=models.PROTECT, null=False)
    granularity = models.IntegerField(null=False)
    time = models.DateTimeField(null=False)
    low = models.DecimalField(max_digits=12, decimdal_places=2, null=False)
    high = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    open = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    close = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    volume = models.DecimalField(max_digits=12, decimal_places=2, null=False)


class TradeSession(models.Model):
    # TODO: Support taking savings out
    start_amount = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    start_time = models.DateTimeField(null=False)
    end_amount = models.DecimalField(max_digits=12, decimal_places=2)
    end_time = models.DateTimeField()
    simulation = models.BooleanField(null=False)
    active = models.BooleanField(null=False)
    creator = models.CharField(max_length=256, null=False)


class Trade(models.Model):
    currency_id = models.ForeignKey(Currency, to_field="currency_id", on_delete=models.PROTECT, null=False)
    trader_id = models.CharField(max_length=256, null=False)
    session = models.ForeignKey(TradeSession, on_delete=models.PROTECT, null=False)
    amount = models.DecimalField(max_digits=12, decimal_places=8, null=False)  # TODO: Is this too many/little?
    price = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    time = models.DateTimeField(null=False)
    notes = models.CharField(max_length=1024)
