#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

def foo():
    print('from foo')
res = foo()
print(res)

# 一：返回None
'''
没有 return
return
return None
以上三种情况都返回 None
'''
# 二：return 一个值 函数调用返回结果就是这个值
# 三：return 值1,值2，...，都还隔开 (值1，值2，...)

a, b, c = (1, 2, 3)  # 元组的解压
x, _, z = (4, 5, 6)
print(a, b, c, x, z)
