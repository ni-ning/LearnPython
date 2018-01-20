#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET 基于网络套接字；SOCK_STREAM流式，即tcp
s.bind(('127.0.0.1', 8080))
s.listen(5)  # 当有多个连接时，挂起一部分，连接池  backlog

print('start...')
conn, addr = s.accept()  # 等着客户端连接：conn三次握手建立的连接，addr客户端
print(conn)
print('clint addr', addr)

print('ready to recv msg...')
client_msg = conn.recv(1024)  # 收消息
print('client_msg: %s' % client_msg)

conn.send(client_msg.upper()) # 发消息

conn.close()
s.close()
