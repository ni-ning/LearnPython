#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 字典
dict1 = {
    'name': 'alex',
    'password': 123456
}

# 根据索引k，获取值
name = dict1['name']
print(name)

# 无：增加；有：修改
dict1['age'] = 18
print(dict1)

# 删除
del dict1['name']
print(dict1)

# for循环
for k, v in dict1.items():
    print(k, v)

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

