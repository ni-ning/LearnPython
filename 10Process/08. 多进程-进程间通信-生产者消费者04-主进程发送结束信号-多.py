#!/usr/bin/env python
# -*-coding:utf-8 -*-

from multiprocessing import Process, Queue
import time
import random


def consumer(q, name):
    while True:
        time.sleep(random.randint(1, 3))
        res = q.get()
        if res is None:
            print('%s 结束...' % name)
            break  # 消费者接收到结束信号跳出死循环
        print('\033[44m消费者%s 拿到了 %s\033[0m' % (name, res))


# 生产者不管消费者什么时候拿，有没有拿到
def producer(seq, q, name):
    for item in seq:
        time.sleep(random.randint(1, 3))
        q.put(item)
        print('生产者 %s 生产了%s' % (name, item))


if __name__ == '__main__':
    q = Queue()

    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q, 'Linda'))
    c2 = Process(target=consumer, args=(q, 'Jonathan'))

    # 生产者们:即厨师们
    seq1 = ['包子%s' % i for i in range(3)]
    p1 = Process(target=producer, args=(seq1, q, '厨师1'))

    seq2 = ['水饺%s' % i for i in range(3)]
    p2 = Process(target=producer, args=(seq2, q, '厨师2'))

    seq3 = ['馒头%s' % i for i in range(3)]
    p3 = Process(target=producer, args=(seq3, q, '厨师3'))

    # 开始
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()    # 必须保证生产者全部生产完毕,才应该发送结束信号
    p2.join()    # 必须保证生产者全部生产完毕,才应该发送结束信号
    p3.join()    # 必须保证生产者全部生产完毕,才应该发送结束信号

    q.put(None)  # 有几个消费者就应该发送几次结束信号None
    q.put(None)  # 有几个消费者就应该发送几次结束信号None

    print('主进程...')


    """
    多生产者多消费者时，则需要等待生产者全部完成，并发送多次结束信号
    """