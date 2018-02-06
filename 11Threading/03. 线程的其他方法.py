#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from threading import Thread
import threading


def work():
    print("%s says hello." % threading.current_thread().getName())


if __name__ == '__main__':
    t = Thread(target=work)

    # t.setDaemon(True)  # 主线程结束后，该守护线程直接结束
    t.start()
    # t.join()  # 主线程等着子线程结束后再执行
    print(threading.enumerate())      # 当前活跃的线程对象，是一个列表形式
    print(threading.active_count())   # 当前活跃线程数
    print('主线程',threading.current_thread())             # 当前线程对象
    print('主线程',threading.current_thread().getName())   # 当前线程名称

