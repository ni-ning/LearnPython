#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from multiprocessing import Process
import random
import time

"""
p1.join() 主进程等着子进程结束
"""


def task(name):
    print('%s is doing task' % name)
    time.sleep(random.randint(1, 3))
    print('%s has finished the task' % name)


if __name__ == '__main__':
    p1 = Process(target=task, args=('Linda',))
    p2 = Process(target=task, args=('Catherine',))
    p3 = Process(target=task, args=('Jonathan',))
    p4 = Process(target=task, args=('Green',))

    """
    Process()哪个先建好，就执行target任务，由操作系统控制顺序
    """
    p1.start()  # 发系统调用，执行顺序由OS控制
    p2.start()  # 发系统调用，执行顺序由OS控制
    p3.start()  # 发系统调用，执行顺序由OS控制
    p4.start()  # 发系统调用，执行顺序由OS控制

    p1.join()  # 主进程调用阻塞自己，主进程等着子进程p1执行完
    p2.join()  # 主进程调用阻塞自己，主进程等着子进程p2执行完
    p3.join()  # 主进程调用阻塞自己，主进程等着子进程p3执行完
    p4.join()  # 主进程调用阻塞自己，主进程等着子进程p4执行完

    """
    # 简便写法
    p_list = [p1, p2, p3, p4]
    for p in p_list:
        p.start()
    for p in p_list:
        p.join()
    """

    # 要有并发思想
    print('父进程')
