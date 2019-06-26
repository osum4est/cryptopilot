from django.db import models


class Currency(models.Model):
    currency_id = models.CharField(max_length=16, unique=True)
    base_currency = models.CharField(max_length=16)
    quote_currency = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=7)  # #ffffff


class Candle(models.Model):
    currency = models.ForeignKey(Currency, to_field="currency_id", on_delete=models.PROTECT)
    granularity = models.IntegerField()
    time = models.DateTimeField()
    low = models.DecimalField(max_digits=12, decimal_places=2)
    high = models.DecimalField(max_digits=12, decimal_places=2)
    open = models.DecimalField(max_digits=12, decimal_places=2)
    close = models.DecimalField(max_digits=12, decimal_places=2)
    volume = models.DecimalField(max_digits=12, decimal_places=2)


class AutoTrader(models.Model):
    trader_id = models.CharField(max_length=256, unique=True)


class TradeSession(models.Model):
    # TODO: Support taking savings out
    trader = models.ForeignKey(AutoTrader, to_field="trader_id", on_delete=models.PROTECT)
    start_amount = models.DecimalField(max_digits=12, decimal_places=2)
    start_time = models.DateTimeField()
    end_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    end_time = models.DateTimeField(null=True)
    simulation = models.BooleanField()
    active = models.BooleanField()
    creator = models.CharField(max_length=256)

    # TODO: Fix these constraints
    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(check=models.Q(active=False, end_amount__isnull=False, end_time__isnull=False),
    #                                name="active_false_end_notnull"),
    #         models.CheckConstraint(check=models.Q(active=True, end_amount__isnull=True, end_time__isnull=True),
    #                                name="active_true_end_null"),
    #     ]


class Trade(models.Model):
    currency = models.ForeignKey(Currency, to_field="currency_id", on_delete=models.PROTECT)
    session = models.ForeignKey(TradeSession, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=8)  # TODO: Is this too many/little?
    price = models.DecimalField(max_digits=12, decimal_places=2)
    time = models.DateTimeField()
    notes = models.CharField(max_length=1024)
