#!/usr/bin/env python
# -*-coding:utf-8 -*-

from multiprocessing import Process, Queue
import time
import random


def consumer(q, name):
    while True:
        time.sleep(random.randint(1, 3))
        res = q.get()
        if res is None: break
        print('\033[44m消费者%s 拿到了 %s\033[0m' % (name, res))


# 生产者不管消费者什么时候拿，有没有拿到
def producer(seq, q, name):
    for item in seq:
        time.sleep(random.randint(1, 3))
        q.put(item)
        print('生产者 %s 生产了%s' % (name, item))
    q.put(None)


if __name__ == '__main__':
    q = Queue()
    c = Process(target=consumer, args=(q, 'Linda'))
    c.start()

    seq = ['包子%s' % i for i in range(10)]
    p = Process(target=producer, args=(seq, q, '厨师1'))
    p.start()
