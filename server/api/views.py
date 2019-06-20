import json
from datetime import datetime, timedelta

from celery.result import AsyncResult
from chartjs.views.lines import BaseLineChartView
from django.db.models import Avg, F, Min, Max
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

from server.api.datatable_view import DatatableView
from server.api.models import Candle, TradeSession, AutoTrader
from server.api.trader.price_downloader import download_prices_task
from server.auto_traders.auto_trader import get_auto_traders, get_auto_trader

# Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

download_task_id = ""


def download_prices(request):
    global download_task_id

    if download_task_id != "":
        return HttpResponseNotAllowed("Download already running.")

    download_task_id = download_prices_task.delay(request.POST['currency_id']).id
    return redirect("/data_loader")


def download_prices_progress(request):
    global download_task_id

    task = AsyncResult(download_task_id)

    if task.state == 'FAILED':
        download_task_id = ""
        return HttpResponse(json.dumps({"error": task.result}), content_type='application/json')

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

    return HttpResponse(json.dumps(data), content_type='application/json')


class AvailableDataTableView(DatatableView):
    model = Candle
    columns = ["currency_id", "start_date", "end_date", "min_price", "max_price"]

    def get_initial_queryset(self):
        return Candle.objects.values("currency_id").annotate(
            start_date=Min("time"), end_date=Max("time"), min_price=Min("low"), max_price=Max("high"))


class TradersTableView(DatatableView):
    model = AutoTrader
    columns = ["trader_id", "name", "description", "version", "last_run", "last_run_return"]

    def get_initial_queryset(self):
        # We have to add the local scripts to the database first, since datatables only work with models
        # TODO: Run this on server startup as well
        for trader in get_auto_traders():
            AutoTrader.objects.update_or_create(trader_id=trader.get_id())

        return AutoTrader.objects.all()

    def get_custom_columns(self, row, column):
        return {
            "name": get_auto_trader(row.trader_id).get_name,
            "description": get_auto_trader(row.trader_id).get_description,
            "version": get_auto_trader(row.trader_id).get_version,
        }


def default_json(value):
    if isinstance(value, datetime):
        return value.strftime("%m/%d/%Y")

    return str(value)


class TradeSessionsTableView(DatatableView):
    model = TradeSession
    columns = ["trader", "start_time", "end_time", "start_amount", "end_amount"]

    def get_initial_queryset(self):
        return TradeSession.objects.filter(trader=self.kwargs["trader_id"])


class PriceHistoryGraphView(BaseLineChartView):
    resolution = 50
    time_lengths = {
        "hour": timedelta(hours=1),
        "day": timedelta(days=1),
        "week": timedelta(weeks=1),
        "month": timedelta(days=30),
        "year": timedelta(days=365)
    }

    def get_labels(self):
        return ["" for i in range(self.resolution)]

    def get_providers(self):
        return [self.kwargs["c_id"]]

    def get_colors(self):
        yield list((242, 169, 0))

    def get_data(self):
        time_multiplier = int(self.kwargs["length"][0])
        total_time = self.time_lengths[self.kwargs["length"][1:]] * time_multiplier
        time_part = total_time / self.resolution
        start_time = datetime.utcnow() - total_time
        end_time = start_time + time_part
        data = []

        for i in range(0, self.resolution):
            data.append(Candle.objects.filter(currency_id=self.kwargs["c_id"], time__gt=start_time, time__lt=end_time)
                        .aggregate(avg=Avg((F("low") + F("high")) / 2))["avg"])
            start_time += time_part
            end_time += time_part

        return [data]
