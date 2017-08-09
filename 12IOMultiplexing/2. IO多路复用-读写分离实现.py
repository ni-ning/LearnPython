#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import socket
import select

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8001))
sk1.listen(5)

sk2 = socket.socket()
sk2.bind(('127.0.0.1', 8002))
sk2.listen(5)


r_inputs = [sk1, sk2]
w_inputs = []

while True:

    r, w, e = select.select(r_inputs, w_inputs, [], 0.05)
    """
    select.select(rlist, wlist, xlist,timeout)

    r 列表存储连接socket对象，可读(针对server而言)
    w 列表存储已发送来数据conn对象，可写(针对server而言)
    读写分离
    """

    for obj in r:
        if obj in [sk1, sk2]:
            # 新连接来了...
            conn, addr = obj.accept()
            print('新连接[%s]来了...' % conn)
            r_inputs.append(conn)
        else:
            # '连接用户发消息了...'
            try:
                data = obj.recv(1024)
                print('连接用户发消息[%s]了...' % data)
            except ConnectionResetError:
                data = ""
            if data:
                # obj.sendall(data)
                w_inputs.append(obj)
            else:
                obj.close()
                r_inputs.remove(obj)
                w_inputs.remove(obj)

    for obj in w_inputs:
        obj.sendall(b'ok')
        w_inputs.remove(obj)
