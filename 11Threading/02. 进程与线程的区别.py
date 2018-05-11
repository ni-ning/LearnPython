#!/usr/bin/env python
# -*-coding:utf-8 -*-

# 1. 开进程的开销远大于线程
"""
发系统调用与主程序执行的关系，就可得出结果
p.start()
t.start()
"""

# 2. 同一进程内的多个线程共享该进程的地址空间
# from multiprocessing import Process
# from threading import Thread
#
# n = 100
# def task():
#     global n
#     n = 1
#
# if __name__ == '__main__':
#     # p = Process(target=task)
#     # p.start()
#     # p.join()
#     # print('Process: n---> ', n)
#     # print('主进程')
#     #
#     t = Thread(target=task)
#     t.start()
#     t.join()
#     print('Thread: n---> ', n)
#     print('主线程')


# 3. 观察一下 os.pid()
from multiprocessing import Process, current_process
from threading import Thread
import os

def task():
    print('task pid: %s' % current_process().pid)

if __name__ == '__main__':
    p = Process(target=task)
    p.start()

    # t = Thread(target=task)
    # t.start()

    print(os.getpid())
    print('main pid: %s' % current_process().pid)
