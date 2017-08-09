#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import socket
sk2 = socket.socket()
sk2.connect(('127.0.0.1', 8002))

while True:
    msg = input('>>: ').strip()

    sk2.send(msg.encode('utf-8'))
    res = sk2.recv(1024)
    print(res)

