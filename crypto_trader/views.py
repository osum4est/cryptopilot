from crypto_trader.trader import price_downloader
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from celery.result import AsyncResult
import json

download_task_id = ""

def download_prices(request):
    global download_task_id

    if download_task_id != "":
        return HttpResponseNotAllowed("Download already running.")

    download_task_id = price_downloader.download_prices.delay().id
    return redirect("/price_history")

def download_prices_progress(request):
    global download_task_id

    task = AsyncResult(download_task_id)
    if (task.state != 'PENDING' and task.state != 'PROGRESS'):
        download_task_id = ""
        task = AsyncResult(download_task_id)
    
    data = {
        'downloading': download_task_id != "",
        'progress': int(float(task.result['current']) / float(task.result['total']) * 100) if download_task_id != "" else 0
    }

    return HttpResponse(json.dumps(data), content_type='application/json')
