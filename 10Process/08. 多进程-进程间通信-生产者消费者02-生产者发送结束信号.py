#!/usr/bin/env python
# -*-coding:utf-8 -*-

from multiprocessing import Process, Queue
import time
import random


def consumer(q, name):
    while True:
        time.sleep(random.randint(1, 3))
        res = q.get()
        if res is None: break  # 消费者接收到结束信号跳出死循环
        print('\033[44m消费者%s 拿到了 %s\033[0m' % (name, res))


# 生产者不管消费者什么时候拿，有没有拿到
def producer(seq, q, name):
    for item in seq:
        time.sleep(random.randint(1, 3))
        q.put(item)
        print('生产者 %s 生产了%s' % (name, item))
    q.put(None)  # 生产者生产完毕后，往队列中再发一个结束信号


if __name__ == '__main__':
    q = Queue()
    c = Process(target=consumer, args=(q, 'Linda'))
    c.start()

    seq = ['包子%s' % i for i in range(10)]
    p = Process(target=producer, args=(seq, q, '厨师1'))
    p.start()


"""
生产者消费者模型总结
1. 程序中有两类角色
    - 一类负责生产数据(生产者)
    - 一类负责处理数据(消费者)
2. 引入生产者消费者模型为了解决的问题是：
    - 平衡生产者和消费者之间的速度差
3. 如何实现：
    生产者 -> 队列 -> 消费者
4. 生产者消费者模型实现类程序的解耦

"""