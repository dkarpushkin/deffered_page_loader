import os
import requests
from time import sleep
from celery import Celery
from celery.result import AsyncResult

app = Celery(
    'tasks',
    broker=f'pyamqp://guest:guest@{os.environ["RABBIT_HOST"]}:5672/',
    backend=f'rpc://guest:guest@{os.environ["RABBIT_HOST"]}:5672/'
)


@app.task()
def task_load_page(url):
    response = requests.get(url)

    # спим 10 секунд чтобы проверить состояние, когда таск еще выполняется
    sleep(10)

    return response.content.decode(response.encoding)


def async_load_page(url):
    result = task_load_page.delay(url)
    print(result.backend)
    return result.id


def async_result(async_id):
    async_task = AsyncResult(async_id, app=app)
    if async_task.ready():
        if async_task.successful():
            return async_task.get(), True
        else:
            return 'Failed', False

    return 'Not ready', False
