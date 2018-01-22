#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的
创建队列的类(底层就是以管道和锁定的方式实现)
"""
# 先进先出
# Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递
from multiprocessing import Process, Queue

q = Queue(maxsize=3)

q.put({'a': 1})
q.put('b')
q.put(3)

# q.put(4)  # 会卡主等待有人取get
# q.put(4, block=False) # 已满，抛出异常  queue.Full
# q.put_nowait(4)       # 等同于 q.put(4, block=False)
# q.put(4, timeout=2)   # 等2秒，抛出异常 queue.Full
print('q.qsize()', q.qsize())  # 判断队列里元素个数
print(q.full())  # 是否已满


print(q.get())
print(q.get())
print(q.get())
# print(q.get())             # 会卡主等待有人put
# print(q.get_nowait())      # 已空，抛出异常，queue.Empty
# print(q.get(block=False))  # 等同于q.get_nowait()
# print(q.get(timeout=2))      # 等2秒，空，抛出异常

print(q.empty())  # 是否已空
