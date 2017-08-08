#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from multiprocessing import Process
from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)


def talk(conn, addr):
    while True:
        try:
            msg = conn.recv(1024)
            print(msg)
            if not msg: break
            conn.send(msg.upper())
        except Exception:
            break

if __name__ == '__main__':
    while True:
        conn, addr = server.accept()
        # 启任务，就是启进程
        p = Process(target=talk, args=(conn, addr),)
        p.start()

"""
来一个连接，就会启一个进程，太多会卡死的
优化：进程池
"""