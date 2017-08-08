#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from socket import *
"""
客户端一直发
服务端一次收
"""

ftp_client = socket(AF_INET, SOCK_STREAM)
ftp_client.connect(('127.0.0.1', 8080))

ftp_client.send('hello'.encode('utf-8'))
ftp_client.send('world'.encode('utf-8'))
ftp_client.send('linda'.encode('utf-8'))

ftp_client.close()