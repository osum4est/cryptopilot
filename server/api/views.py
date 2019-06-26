from datetime import datetime, timedelta

from celery.result import AsyncResult
from chartjs.views.lines import BaseLineChartView
from django.db.models import Avg, F, Min, Max
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from server.api.models import Candle, TradeSession, AutoTrader, Currency
from server.api.serializers import TraderSerializer, CandleOverviewSerializer, CurrencySerializer, \
    TradeSessionSerializer
from server.api.trader.price_downloader import download_prices_task
from server.auto_traders.auto_trader import get_auto_traders

# Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

download_task_id = ""


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Currency.objects.all().order_by("currency_id")
    serializer_class = CurrencySerializer
    lookup_field = "currency_id"


class CandlesDownloadViewSet(ViewSet):
    def list(self, request):
        global download_task_id

        task = AsyncResult(download_task_id)

        if task.state == 'FAILED':
            download_task_id = ""
            return Response({"error": task.result})

        if task.state != 'PENDING' and task.state != 'PROGRESS':
            download_task_id = ""
            task = AsyncResult(download_task_id)

        data = {
            'downloading': download_task_id != "",
        }

        if task.state == "PROGRESS":
            data["progress"] = int(
                float(task.result['current']) / float(task.result['total']) * 100) if download_task_id != "" else 0
        else:
            data["progress"] = "0"

        return Response(data)

    def create(self, request):
        global download_task_id

        if "currency_id" not in request.data:
            return Response({"message": "Include currency id"}, status=status.HTTP_400_BAD_REQUEST)

        if download_task_id != "":
            return Response({"message": "Already downloading data"}, status=status.HTTP_409_CONFLICT)

        download_task_id = download_prices_task.delay(request.data['currency_id']).id
        return Response(status=status.HTTP_200_OK)


class CandleOverviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Candle.objects.values("currency_id").annotate(
        start_date=Min("time"), end_date=Max("time"), min_price=Min("low"), max_price=Max("high"))
    serializer_class = CandleOverviewSerializer


class TraderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AutoTrader.objects.all().order_by("trader_id")
    serializer_class = TraderSerializer

    def get_queryset(self):
        # We have to add the local scripts to the database first, since datatables only work with models
        # TODO: Run this on server startup as well
        for trader in get_auto_traders():
            AutoTrader.objects.update_or_create(trader_id=trader.get_id())

        return self.queryset


class TradeSessionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TradeSession.objects.all().order_by("id")
    serializer_class = TradeSessionSerializer
    filterset_fields = ("trader",)


class PriceHistoryChartView(BaseLineChartView, ViewSet):
    resolution = 50
    time_lengths = {
        "hour": timedelta(hours=1),
        "day": timedelta(days=1),
        "week": timedelta(weeks=1),
        "month": timedelta(days=30),
        "year": timedelta(days=365)
    }

    def list(self, request):
        if "currency_id" not in request.query_params:
            return Response({"message": "Include currency id"}, status=status.HTTP_400_BAD_REQUEST)
        if "length" not in request.query_params:
            return Response({"message": "Include length"}, status=status.HTTP_400_BAD_REQUEST)
        return super(PriceHistoryChartView, self).get(request)

    def get_labels(self):
        return ["" for i in range(self.resolution)]

    def get_providers(self):
        return [self.request.query_params["currency_id"]]

    def get_colors(self):
        color = Currency.objects.filter(currency_id=self.request.query_params["currency_id"]).first().color
        color = color.lstrip("#")
        yield list(tuple(int(color[i:i+2], 16) for i in (0, 2, 4)))

    def get_data(self):
        time_multiplier = int(self.request.query_params["length"][0])
        total_time = self.time_lengths[self.request.query_params["length"][1:]] * time_multiplier
        time_part = total_time / self.resolution
        start_time = datetime.utcnow() - total_time
        end_time = start_time + time_part
        data = []

        for i in range(0, self.resolution):
            data.append(Candle.objects.filter(currency_id=self.request.query_params["currency_id"], time__gt=start_time, time__lt=end_time)
                        .aggregate(avg=Avg((F("low") + F("high")) / 2))["avg"])
            start_time += time_part
            end_time += time_part

        return [data]
