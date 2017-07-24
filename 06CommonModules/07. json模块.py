#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 内存数据断电消失，需要存到磁盘上。内存中有数据结构概念(列表、字典、字符串等)，但是磁盘上都是字符串
# 场景：虚拟机快照、游戏存档  --> 运行数据结构按照特定格式存到磁盘上


"""
eval内置方法可以将一个字符串转成python对象，不过，eval方法是有局限性的
eval的重点还是通常用来执行一个字符串表达式，并返回表达式的值
"""
import json
x = "[null, true, false, 1]"
# print(eval(x))      # 报错，无法解析null, true, false
print(json.loads(x))  # json就可以, [None, True, False, 1]


dic = {
    "name": "Linda",
    "age": 18,
    "sex": "female",
}

with open('a.txt', 'w', encoding='utf-8') as f:
    f.write(str(dic))

with open('a.txt', 'r',encoding='utf-8') as f2:
    res = eval(f2.read())
    print(res, type(res))

"""
什么是序列化？
我们把对象(变量)从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等

为什么要序列化？
1：持久保存状态
2：跨平台数据交互
对接只能是数据，Python的字典与Java的字典如何对接
如果收发的双方约定好实用一种序列化的格式，那么便打破了平台/语言差异化带来的限制，实现了跨平台数据交互
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

"""
# json特点
"""
JSON            Python
{}              dict
[]              list
"string"        str
123.45          int或float
true/false      True/Fase
null            None

但是如set，tuple等json就不支持了，但适合快平台
"""

# pickle  可以序列化所有的Python数据类型，但是不适合跨平台

import pickle
x = b"[null, true, false, 1]"
# pickle.loads(x) # 报错，x 不是 Python语法

# json用法
# 序列化的过程：dic --> res=json.dumps(dic) ---> f.write(res)
dic = {
    "name": "Linda",
    "age": 18,
    "sex": "female",
}

res = json.dumps(dic)
print(res, type(res))  # {"sex": "female", "name": "Linda", "age": 18} <class 'str'>
with open('a.json', 'w') as f3:
    f3.write(res)


# 返序列化过程： res = f.read()  --> res = json.loads(res)  --> dic=res
with open('a.json', 'r') as f4:
    dic = json.loads(f4.read())

print(dic, type(dic))
print(dic['name'])

# json便捷操作  json.dump(obj,fp_w)   dic=json.load(fp_r)

dic = {
    "name": "Linda",
    "age": 18,
    "sex": "female",
}

json.dump(dic, open('b.json', 'w'))

res = json.load(open('b.json', 'r'))
print(dic, type(dic))

"""
数据流转：

内存中结构化的数据  <-->  json格式数据  <-->   字符串   <--> 保存到文件中或基于网络传输
"""




















