#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com
import time

# 加工的是函数，授权实现
class Open(object):
    def __init__(self, filepath, mode='r', encoding='utf-8'):
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding
        self.f = open(self.filepath, mode=self.mode, encoding=self.encoding)

    def write(self, msg):
        t = time.strftime('%Y-%m-%d %X')
        self.f.write('%s %s' % (t, msg))
    def __getattr__(self, item):
        return getattr(self.f, item)

obj = Open('a.txt', mode='w')
obj.write('1111111111111\n')
time.sleep(2)
obj.write('2222222222222\n')
time.sleep(1)
obj.write('3333333333333\n')
obj.close()