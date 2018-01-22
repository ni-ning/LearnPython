#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
希望函数的某些参数强制使用关键字函数
"""


# 将强制关键字参数放到某个*参数或者单个*后面就能达到这个效果
def recv(maxsize, *, block):
    pass


# recv(1024, True)  # TypeError
recv(1024, block=True)


"""
使用强制关键字会比使用位置参数表意更加清晰  msg = recv(1024, block=False)
"""

