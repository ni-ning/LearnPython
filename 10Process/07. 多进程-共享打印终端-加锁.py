#!/usr/bin/env python
# -*-coding:utf-8 -*-

from multiprocessing import Process, Lock
import os
import time

"""
并发运行,效率高,但竞争同一打印终端,带来了打印错乱
加锁：由并发变成了串行,牺牲了运行效率,但避免了竞争
"""


def work(lock):
    lock.acquire()
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock, ))
        p.start()

