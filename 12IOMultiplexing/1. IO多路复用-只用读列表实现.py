#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import socket
import select

"""
一个线程如何监听多个端口号
IO 多路复用：监听8001,8002
"""

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8001))
sk1.listen(5)

sk2 = socket.socket()
sk2.bind(('127.0.0.1', 8002))
sk2.listen(5)

# conn, addr = sk1.accept() # 当客户端发来连接，阻塞终止，往下执行
# print(type(conn))         # <class 'socket.socket'>，conn也是socket对象，会被select监听
# conn.recv(1024)           # 当客户端发来数据，阻塞终止，往下执行

inputs = [sk1, sk2]
while True:
    # IO 多路复用：同时监听多个socket对象，创造出并发
    #   - select 内部进行循环操作(监听socket有个数，最大1024)，主动查看，Windows只有select
    #   - poll  内部进行循环操作(监听无个数限制)，主动查看
    #   - epoll 内部异步回调(监听无个数限制)，被动告知，如nginx内部实现原理

    r, w, e = select.select(inputs, [], [], 0.05)  # 监听socket对象是否变化
    # r = [sk1, ]
    # r = [sk2, ]
    # r = [sk1, sk2, ]
    # r = []
    # 实现监听 sk1和sk2对象，看看有哪些需要连接

    # 已建立连接，等待接收数据的socket对象conn
    # r = [sk1, sk2, conn]
    # r = [sk1, sk2,]
    # r = [conn,]
    for obj in r:
        if obj in [sk1, sk2]:
            # 新连接来了...
            conn, addr = obj.accept()
            print('新连接[%s]来了...' % conn)
            inputs.append(conn)
        else:
            # '连接用户发消息了...'
            data = obj.recv(1024)
            print('连接用户发消息[%s]了...' % data)
            obj.sendall(data)
