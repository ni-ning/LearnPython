#!/usr/bin/env python
# -*-coding:utf-8 -*-

from multiprocessing import Process
import os
import time

"""
并发运行,效率高,但竞争同一打印终端,带来了打印错乱
"""


def work():
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())


if __name__ == '__main__':

    for i in range(3):
        p = Process(target=work)
        p.start()

