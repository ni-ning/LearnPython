#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import socket
"""
有两个地方会卡住
1. conn, addr = s.accept()       # 等着客户端连接
2. client_msg = conn.recv(1024)  # 等着客户端发消息

注意点：
1. 避免客户端主动终止服务 Windows: try...except   Linux: if not client_msg: break
2. 链接循环 服务端服务多个客户端
3. 通信循环 链路建立后，可以来回通信
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # AF_INET 基于网络套接字；SOCK_STREAM流式，即tcp
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 四次挥手，time_wait 优化
s.bind(('127.0.0.1', 8080))
s.listen(5)  # 当有多个连接时，挂起一部分，连接池  backlog

while True:  # 链接循环，循环建链接
    print('starting...')
    conn, addr = s.accept()  # 等着客户端连接：conn三次握手建立的连接，addr客户端
    print('client addr',addr)

    while True:  # 与conn的通信循环
        try:      # try 是为了避免客户端主动终止服务，而报的异常，针对Windows
            client_msg = conn.recv(1024)   # 收消息
            if not client_msg: break       # Linux平台，不会报错，但会一直收空
            print('client msg:', client_msg)
            conn.send(client_msg.upper())  # 发消息
        except ConnectionResetError as e:
            break
    conn.close()
