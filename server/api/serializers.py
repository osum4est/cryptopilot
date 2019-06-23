from rest_framework import serializers

from server.api.models import AutoTrader, Candle, Currency, TradeSession
from server.auto_traders.auto_trader import get_auto_trader


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='currency-detail',
        lookup_field='currency_id'
    )

    class Meta:
        model = Currency
        fields = ('url', 'currency_id', 'base_currency', 'quote_currency', 'name')


class CandleOverviewSerializer(serializers.HyperlinkedModelSerializer):
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    min_price = serializers.DecimalField(max_digits=12, decimal_places=2)
    max_price = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        model = Candle
        fields = ("currency_id", "start_date", "end_date", "min_price", "max_price")


class TraderSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    version = serializers.SerializerMethodField()

    @staticmethod
    def get_name(obj):
        return get_auto_trader(obj.trader_id).get_name()

    @staticmethod
    def get_description(obj):
        return get_auto_trader(obj.trader_id).get_description()

    @staticmethod
    def get_version(obj):
        return get_auto_trader(obj.trader_id).get_version()

    class Meta:
        model = AutoTrader
        fields = ('url', 'trader_id', 'name', 'description', 'version')


class TradeSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TradeSession
        fields = ("url", "id", "trader", "start_amount", "start_time", "end_amount", "end_time", "simulation", "active",
                  "creator")
