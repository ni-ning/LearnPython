#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from multiprocessing import Process
import random
import time

"""
主进程运行完，子进程也都回收掉
"""


def task(name):
    print('%s is doing task' % name)
    time.sleep(random.randint(1, 3))
    print('%s has finished the task' % name)


if __name__ == '__main__':
    p1 = Process(target=task, args=('Linda',))
    p1.daemon = True  # 守护进程
    p1.start()

    print('父进程')
    print(p1.name)
    print(p1.pid)
