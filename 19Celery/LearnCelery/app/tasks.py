#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

# 所有的app都可以调用
@shared_task
def add(x, y):
    time.sleep(10)
    return x + y

@shared_task
def mul(x, y):
    time.sleep(10)
    return x * y