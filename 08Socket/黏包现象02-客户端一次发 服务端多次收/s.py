#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
from socket import *

ftp_server = socket(AF_INET, SOCK_STREAM)
ftp_server.bind(('127.0.0.1', 8080))
ftp_server.listen(5)

conn, addr = ftp_server.accept()
res1 = conn.recv(1)  # 有就收走，没有就卡在原地
res2 = conn.recv(1)  # 有就收走，没有就卡在原地
res3 = conn.recv(1)  # 有就收走，没有就卡在原地
print(res1.decode('utf-8'))
print(res2.decode('utf-8'))
print(res3.decode('utf-8'))

conn.close()
ftp_server.close()
