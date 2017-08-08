#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))  # 建立连接--> 对应服务端 s.accept()
while True:  # 通信循环
    msg = input('>>: ').strip()
    if not msg: continue   # 防止客户端发空
    client.send(msg.encode('utf-8')) # 发消息-->  对应服务端 s.read()

    back_msg = client.recv(1024)

    print('back msg: ', back_msg.decode('utf-8'))

client.close()
