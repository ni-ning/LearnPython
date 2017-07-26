#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


class FtpClient:

    def __init__(self, host):
        self.host = host
        print('connecting [%s]...' % self.host)


    def run(self):
        while True:
            inp = input('>>: ').strip()  # 用户输入的是字符串
            inp_list = inp.split()
            if hasattr(self, inp_list[0]):
                func = getattr(self, inp_list[0])
                func(inp_list)

    def get(self, arg):
        print('download file...', arg[1])

f = FtpClient('192.168.1.1')
f.run()
