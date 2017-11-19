#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

from spam import money
print(money)

# from...import...干的事情
'''
1. 产生新的名称空间
2. 以新建的名称空间为全局名称空间，执行文件的代码
3. 直接拿到spam.py名称空间中的名字
'''

"""
from...import...
优点：方便，不加前缀
缺点：容易跟当前文件的名称空间冲突
"""

from spam import *

read1()
# read2()  # 报错，因spam.__all__没定义

