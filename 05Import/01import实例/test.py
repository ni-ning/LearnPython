#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

import spam

# 导入模块干的事
'''
1. 产生新的名称空间
2. 以新建的名称空间为全局名称空间，执行文件的代码
3. 拿到一个模块名spam，指向spam.py产生的名称空间
'''
money = 100000000
print(spam.money)  # 1000
print(spam.read1)
spam.read1()       # spam模块： 1000
spam.read2()       # spam模块中的read1()

