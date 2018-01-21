#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

from multiprocessing import Process


def task(filename, msg):
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(msg)

if __name__ == '__main__':
    for i in range(5):
        p = Process(target=task, args=('a.txt', "进程 %s\n" % str(i)))
        p.start()
