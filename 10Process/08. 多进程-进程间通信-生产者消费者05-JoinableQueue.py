#!/usr/bin/env python
# -*-coding:utf-8 -*-

from multiprocessing import Process, JoinableQueue
import time
import random


def consumer(q, name):
    while True:
        time.sleep(random.randint(1, 3))
        res = q.get()
        print('\033[44m消费者%s 拿到了 %s\033[0m' % (name, res))

        q.task_done()  # 向q.join()发送一次信号,证明一个数据已经被取走了


# 生产者不管消费者什么时候拿，有没有拿到
def producer(seq, q, name):
    for item in seq:
        time.sleep(random.randint(1, 3))
        q.put(item)
        print('生产者 %s 生产了%s' % (name, item))

    q.join()
    print('%s 完成生产了...' % name)


if __name__ == '__main__':
    q = JoinableQueue()

    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q, 'Linda'))
    c2 = Process(target=consumer, args=(q, 'Jonathan'))
    c1.daemon = True
    c2.daemon = True

    # 生产者们:即厨师们
    seq1 = ['包子%s' % i for i in range(3)]
    p1 = Process(target=producer, args=(seq1, q, '厨师1'))

    seq2 = ['水饺%s' % i for i in range(3)]
    p2 = Process(target=producer, args=(seq2, q, '厨师2'))

    seq3 = ['馒头%s' % i for i in range(3)]
    p3 = Process(target=producer, args=(seq3, q, '厨师3'))

    # 开始
    process_list = [p1, p2, p3, c1, c2]
    for p in process_list:
        p.start()

    p1.join()
    p2.join()
    p3.join()
    print('主进程...')

    """
    主进程等 --> p1,p2,p3等 --> c1,c2
    p1,p2,p3结束了，证明c1,c2肯定全都收完了p1,p2,p3发送到队列的数据
    因而c1,c2也就没有存在的价值了，应该随着主进程的结束而结束，所以设置成守护进程
    """