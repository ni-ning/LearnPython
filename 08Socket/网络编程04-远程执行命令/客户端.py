#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))  # 建立连接--> 对应服务端 s.accept()
while True:  # 通信循环
    cmd = input('>>: ').strip()
    if not cmd: continue   # 防止客户端发空
    client.send(cmd.encode('utf-8')) # 发消息-->  对应服务端 s.recv(1024)

    cmd_res = client.recv(1024)

    print(cmd_res.decode('gbk'))   # subprocess结果默然编码为 平台编码 gbk

