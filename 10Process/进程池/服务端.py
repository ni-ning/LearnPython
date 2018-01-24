#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from multiprocessing import Pool
from socket import *
import os

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)


def talk(conn, addr):
    print(os.getpid())
    while True:
        try:
            msg = conn.recv(1024)
            # print(msg, 'from addr', addr)
            if not msg:
                break
            conn.send(msg.upper())
        except Exception:
            break


if __name__ == '__main__':
    res_l = []
    pool = Pool(3)  # 只建一个pool池

    while True:
        conn, addr = server.accept()

        # pool.apply(talk, args=(conn, addr))  # 必须得等着其中一个talk结束，才进行下一个

        res = pool.apply_async(talk, args=(conn, addr))
        res_l.append(res)
        # print(res)


