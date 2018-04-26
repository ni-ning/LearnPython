#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
对象兼容 with语句，需实现__enter__()和__exist__()方法
"""
from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection(object):
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

"""
这个类的关键点在于表示了一个网络连接，但是初始化的时候不会做任何事情(比如它并没有建立一个连接)
连接的建立和关闭是使用with语句自动完成
"""
from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # print(resp)

"""
当出现with语句的时候，对象的__enter__()方法触发，它返回值(如果有)会被赋值给as声明的变量
然后，with语句块里面的代码开始执行，
最后，__exit__()方法被触发进行清理工作，即使有异常也会处理
"""

"""
# 允许多个with嵌套
from socket import socket, AF_INET, SOCK_STREAM
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()

conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s2:
        pass
"""

# 总结
"""
上下文使用场景：文件、网络连接和锁的编程环境中
主要共同特征：它们必须被手动关闭或释放来确保程序的正确运行，比如请求了一个锁，使用完以后要释放，否则可能产生死锁
"""