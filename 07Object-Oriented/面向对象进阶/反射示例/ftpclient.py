#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


class FtpClient:
    """ftp客户端,但是还么有实现具体的功能"""

    def __init__(self, addr):
        print('正在连接服务器[%s]' % addr)
        self.addr = addr

    # def get(self):
    #     print('get....')

