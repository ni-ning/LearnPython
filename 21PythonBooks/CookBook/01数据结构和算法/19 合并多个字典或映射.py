#!/usr/bin/env python
# -*-coding:utf-8 -*-


# 将多个字典或映射，合并为单一映射后执行某些操作，如查找某些键或值是否存在
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}


from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])  # from a
print(c['y'])  # from b
print(c['z'])  # from a，重复键，返回第一次值

# del c['y']  # 会抛出异常
# 对于字典 c 的更新或删除操作总是影响的是列表中第一个字典

"""
当然可以考虑 update()，但是会创建一个完全不同的字典对象
"""