import time
from celery import shared_task, current_task

@shared_task
def download_prices():
    for i in range(10):
        current_task.update_state(state='PROGRESS',
                                  meta={'current': i, 'total': 10})
        time.sleep(1)
    print("Doing stuff")