#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 单独脚本调用Django内容时，需配置脚本的环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearnCelery.settings')

app = Celery('mysite')

#  CELERY_ 作为前缀，在settings中写配置
app.config_from_object('django.conf:settings', namespace='CELERY')

# 到Django各个app下，自动发现tasks.py 任务脚本
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))