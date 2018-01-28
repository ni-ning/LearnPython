#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from threading import Thread
import os


def work():
    print("%s says hello." % os.getpid())

if __name__ == '__main__':
    t = Thread(target=work)
    t.start()

    print('主线程:', os.getpid())   # 与线程的pid相同
