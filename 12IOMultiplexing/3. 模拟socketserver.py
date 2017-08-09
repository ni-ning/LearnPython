#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import socket
import select
import threading


def process_request(conn):  #
    while True:
        v = conn.recv(1024)
        print(v)
        conn.sendall(b'okkk')

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8001))
sk1.listen(5)

inputs = [sk1, ]
while True:
    r, w, e = select.select(inputs, [], inputs, 0.05)
    for obj in r:
        if obj in [sk1, ]:
            # 客户端的socket
            conn, addr = obj.accept()
            t = threading.Thread(target=process_request, args=(conn,))
            t.start()


