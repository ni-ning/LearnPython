#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import socket
sk1 = socket.socket()
sk1.connect(('127.0.0.1', 8001))

while True:
    msg = input('>>: ').strip()

    sk1.send(msg.encode('utf-8'))
    res = sk1.recv(1024)
    print(res)