import json
from datetime import datetime, timedelta

from celery.result import AsyncResult
from chartjs.views.lines import BaseLineChartView
from django.db.models import Avg, F, Min, Max
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect

from auto_traders.auto_trader import get_auto_traders
from crypto_trader.models import Candle
from crypto_trader.trader.price_downloader import download_prices_task

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


def get_available_data(request):
    data = [["Currency", "Start Date", "End Date", "Min Price", "Max Price"]]
    data.extend(
        [list(d.values()) for d in
         Candle.objects.values("currency_id").annotate(Min("time"), Max("time"), Min("low"), Max("high"))])
    return HttpResponse(json.dumps(data, default=default_json), content_type='application/json')


def get_available_traders(request):
    data = [["ID", "Name", "Description", "Version", "Last Run", "Last Run Profits"]]
    data.extend(
        [[t.get_id(), t.get_name(), t.get_description(), t.get_version()] for t in get_auto_traders()]
    )
    return HttpResponse(json.dumps(data), content_type='application/json')


def default_json(value):
    if isinstance(value, datetime):
        return value.strftime("%m/%d/%Y")

    return str(value)


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
