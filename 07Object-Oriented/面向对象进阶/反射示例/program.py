#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import ftpclient

# from module import FtpClient
f1 = ftpclient.FtpClient('192.168.1.1')

if hasattr(f1, 'get'):
    func = getattr(f1, 'get')
    func()

print('执行其他代码....')
print('执行其他代码....')
print('执行其他代码....')