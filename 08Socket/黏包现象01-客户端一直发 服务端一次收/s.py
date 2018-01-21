#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from socket import *

ftp_server = socket(AF_INET, SOCK_STREAM)
ftp_server.bind(('127.0.0.1', 8080))
ftp_server.listen(5)

conn, addr = ftp_server.accept()
res = conn.recv(10000000)
print(res.decode('utf-8'))

conn.close()
ftp_server.close()
