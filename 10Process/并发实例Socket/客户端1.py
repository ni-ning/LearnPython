#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

from socket import *
client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    msg = input(">>: ").strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))

    msg = client.recv(1024)
    print(msg.decode('utf-8'))