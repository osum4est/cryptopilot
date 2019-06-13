from django.db import models


class Currency(models.Model):
    currency_id = models.CharField(max_length=16, unique=True, null=False)
    base_currency = models.CharField(max_length=16)
    quote_currency = models.CharField(max_length=16)


class Candle(models.Model):
    currency_id = models.CharField(max_length=16, unique=True, null=False)
    granularity = models.IntegerField()
    time = models.BigIntegerField()
    low = models.DecimalField(max_digits=12, decimal_places=4)
    high = models.DecimalField(max_digits=12, decimal_places=4)
    open = models.DecimalField(max_digits=12, decimal_places=4)
    close = models.DecimalField(max_digits=12, decimal_places=4)
    volume = models.BigIntegerField()
