import json

from celery.result import AsyncResult
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import redirect

from crypto_trader.trader.price_downloader import download_prices_task

download_task_id = ""


def download_prices(request):
    global download_task_id

    if download_task_id != "":
        return HttpResponseNotAllowed("Download already running.")

    download_task_id = download_prices_task.delay(request.POST['currency_id']).id
    return redirect("/price_history")


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
