#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from multiprocessing import Process
import random
import time


def task(name):
    print('%s is doing task' % name)
    time.sleep(random.randint(1, 3))
    print('%s has finished the task' % name)


if __name__ == '__main__':
    p1 = Process(target=task, args=('Linda',))

    p1.start()
    p1.terminate()  # p1 is killed, 但是p1的子进程却不回收，这些子进程会成为僵尸进程
    print(p1.is_alive())
    print(p1.is_alive())
    print(p1.is_alive())
    time.sleep(1)
    print(p1.is_alive())
    print(p1.is_alive())

    print('父进程')

