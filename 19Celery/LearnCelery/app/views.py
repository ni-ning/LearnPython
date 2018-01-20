from django.shortcuts import HttpResponse
from app import tasks
import random
from celery.result import AsyncResult


def celery_call(request):
    t = tasks.add.delay(1, random.randint(0,99))
    return HttpResponse(t.id)


def celery_res(request):
    task_id = request.GET.get('id')
    res = AsyncResult(id=task_id)
    if res.ready():
        result = res.get()
    else:
        result = res.ready()
    return HttpResponse(result)





